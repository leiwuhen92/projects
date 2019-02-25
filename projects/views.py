from pyramid.view import view_config
from pyramid.response import Response
import json

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
# /howdy
@view_config(route_name='howdy',renderer='templates/howdy.pt')
def howdy(request):
    return {'name': 'howdy'}
