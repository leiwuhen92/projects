from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    my_session_factory = SignedCookieSessionFactory('itsaseekreet')  #chapter17
    config = Configurator(settings=settings,session_factory=my_session_factory)

    config.include('pyramid_jinja2')
    config.include('pyramid_chameleon')

    config.add_static_view(name='static', path='projects:static', cache_max_age=3600)  #添加静态资产
    config.add_route('home', '/')


##########################################################################
    ##函数视图
    config.add_route('hello', '/hello')
    config.add_route('hi', '/hi')

    ##类视图
    config.add_route('one', '/one')
    config.add_route('two', '/two')

    config.add_route('plain','/plain')

    config.add_route('chapter11', '/chapter11/{first}/{last}')

    config.add_route('chapter14_json', '/chapter14.json')

    config.add_route('chapter15', '/chapter15/{first}/{last}')
    config.add_route('home15', '/chapter15')


    config.scan('.views')
    return config.make_wsgi_app()
