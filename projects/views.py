from pyramid.view import (
    view_config,
    view_defaults
    )
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound


import logging
logger=logging.getLogger(__name__)

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

    @property
    def counter(self):
        session = self.request.session
        if 'counter' in session:
            session['counter'] += 1
        else:
            session['counter'] = 1

        return session['counter']

    @view_config(route_name='one')
    def one(self):
        #return {'name': 'one'}
        return HTTPFound(location='/plain')  #重定向

    @view_config(route_name='two')
    @view_config(route_name='chapter14_json', renderer='json')
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



@view_defaults(route_name='chapter15')
class chapter15(object):
    def __init__(self, request):
        self.request = request

    @property
    def full_name(self):
        first = self.request.matchdict['first']
        last = self.request.matchdict['last']
        return first + ' ' + last

    @view_config(route_name='home15', renderer='templates/home15.pt')
    def home(self):
        logger.info('Home 15 view')
        return {'page_title': 'Home15 View'}

    @view_config(renderer='templates/chapter15.pt')
    def chapter15(self):
        return {'page_title': 'chapter15 View'}

    @view_config(request_method='POST', renderer='templates/edit15.pt')
    def edit15(self):
        new_name = self.request.params['new_name']
        return {'page_title': 'Edit View', 'new_name': new_name}

    @view_config(request_method='POST', request_param='form.delete',renderer='templates/delete15.pt')
    def delete(self):
        print('Deleted')
        return {'page_title': 'Delete View'}
