from pyramid.config import Configurator



def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    config.include('pyramid_jinja2')
    config.include('pyramid_chameleon')

    config.add_static_view('static', 'static', cache_max_age=3600)
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


    config.scan('.views')
    return config.make_wsgi_app()
