import datetime

from pyramid.decorator import reify
from pyramid.events import subscriber
from pyramid.events import BeforeRender
from pyramid.url import resource_url
from pyramid.url import route_url
from pyramid.url import static_url


class Url(object):
    """View into application- and context state."""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @reify
    def resource_url(self):
        '''
        BBB: conetext_url is for B/C. The method in pyramid is now
        BBB: resource_url
        provides a url given a context
        '''
        return resource_url(self.context, self.request)

    @reify
    def base_url(self):
        '''
        provides a base url given a request
        '''

        url = self.request.url

        view_name = getattr(self.request, 'view_name', None)
        if view_name:
            url = url[:-len(view_name)]

        return url.rstrip('/')

    @reify
    def app_url(self):
        """
        provieds the application's base URL

        .. code-block:: xml

            Hello <a href="${url.app_url}/user/${logged_in}" class="user">
        """
        return self.request.application_url

    def route_url(self, route_name, **kw):
        """
        provides a route url for the application, given a ``route_name``

        .. code-block:: xml

            <a href="${url.route_url('example_view',slug=context._id)}"
            title="example">Example link</a>
        """

        return route_url(route_name, self.request, **kw)

    @reify
    def static_url(self):
        """
        provides the base of the static URL

        .. code-block:: xml

           <link rel="shortcut" href="${url.static_url}images/icon.png" />
        """
        return static_url('atemplate:static/', self.request)

    # @reify
    # def deform_static(self):
    #     """
    #     provides the base of the static URL

    #     .. code-block:: xml

    #        <link rel="example" href="${url.deform_static}images/example.png" />

    #     """
    #     return static_url('deform:static/', self.request)


@subscriber(BeforeRender)
def add_global(event):
    context = event.get('context', None)
    request = event.get('request', None)
    event['date'] = datetime.datetime.now()
    event['section'] = request.get('view_name', request.matched_route.name \
        if request.matched_route else u'common')
    event['url'] = Url(context, request)
