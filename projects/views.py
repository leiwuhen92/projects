from pyramid.view import (
    view_config,
    view_defaults
    )
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'projects'}

##############################################################################
# First view, available at http://localhost:6543/
@view_config(route_name='hi')
def hi(request):
    return Response('<body>Visit <a href="/hello">hello</a></body>')



@view_config(route_name='hello')
def hello(request):
    return Response('<body>Go back <a href="/hi">hi</a></body>')



############################模板##################################
@view_defaults(renderer='templates/howdy.pt')
class projectsviews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='one')
    def one(self):
        #return {'name': 'one'}
        return HTTPFound(location='/plain')  #重定向

    @view_config(route_name='two')
    def two(self):
        return {'name': 'two'}

    @view_config(route_name='plain')
    def plain(self):
        name=self.request.params.get('name','No Name Provided')  #接收前端传来的params
        body = 'URL %s with name: %s' % (self.request.url, name)
        return Response(
            content_type='text/plain',
            body=body
        )



@view_config(route_name='chapter11',renderer='templates/chapter11.pt')
def chapter11(request):
    first = request.matchdict['first']
    last = request.matchdict['last']
    return {
            'name': 'Home View',
            'first': first,
            'last': last
        }