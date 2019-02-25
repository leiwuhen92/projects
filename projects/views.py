from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'projects'}

##############################################################################
# First view, available at http://localhost:6543/
@view_config(route_name='hi')
def hi(request):
    return Response('<body>Visit <a href="/hello">hello</a></body>')


# /howdy
@view_config(route_name='hello')
def hello(request):
    return Response('<body>Go back <a href="/hi">hi</a></body>')