from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig

#from lumin.session import LuminSessionFactoryConfig


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # default_session_factory = LuminSessionFactoryConfig(
    #     settings['secret'],
    #     )
    config = Configurator(
        settings=settings,
        #session_factory=default_session_factory,
        session_factory=UnencryptedCookieSessionFactoryConfig(
            secret=settings['secret'])
        )
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
