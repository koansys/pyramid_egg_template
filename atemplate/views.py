from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/main.pt')
def my_view(request):
    return {'project': 'atemplate',
            'title': "atemplate"}
