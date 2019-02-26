from pyramid.view import (
    view_config,
    view_defaults
    )
from pyramid.response import Response


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
        return {'name': 'one'}

    @view_config(route_name='two')
    def two(self):
        return {'name': 'two'}
