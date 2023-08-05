import json
import uuid
import munch

from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.routing import Map, Rule

__version__ = '0.1.1'

class SolaceResponse(Response):
    json = None

    def __init__(self,):
        super().__init__()

class App:
    
    def __init__(self):
        self.rules = Map([])
        self.views = {}
    
    def __rule(self, method, urlpath, handler):
        uid = str(uuid.uuid4())
        self.rules.add(
            Rule(
                urlpath, 
                endpoint=uid,
                methods=[method]
            )
        )
        self.views[uid] = handler

    def get(self, urlpath, handler):
        """
        The GET method requests a representation of the 
        specified resource. Requests using GET should only 
        retrieve data.
        """
        self.__rule('GET', urlpath, handler)

    def head(self, urlpath, handler):
        """
        The HEAD method asks for a response identical to that
        of a GET request, but without the response body.
        """
        self.__rule('HEAD', urlpath, handler)

    def post(self, urlpath, handler):
        """
        The POST method is used to submit an entity to the 
        specified resource, often causing a change in state
        or side effects on the server.
        """
        self.__rule('POST', urlpath, handler)

    def put(self, urlpath, handler):
        """
        The PUT method replaces all current representations 
        of the target resource with the request payload.
        """
        self.__rule('PUT', urlpath, handler)

    def delete(self, urlpath, handler):
        """
        The DELETE method deletes the specified resource.
        """
        self.__rule('DELETE', urlpath, handler)

    def connect(self, urlpath, handler):
        """
        The CONNECT method establishes a tunnel to the server 
        identified by the target resource.
        """
        self.__rule('CONNECT', urlpath, handler)

    def options(self, urlpath, handler):
        """
        The OPTIONS method is used to describe the communication
        options for the target resource.
        """
        self.__rule('OPTIONS', urlpath, handler)

    def trace(self, urlpath, handler):
        """
        The TRACE method performs a message loop-back test along 
        the path to the target resource.
        """
        self.__rule('TRACE', urlpath, handler)

    def patch(self, urlpath, handler):
        """
        The PATCH method is used to apply partial modifications
        to a resource.
        """
        self.__rule('PATCH', urlpath, handler)

    def __dispatch(self, req):
        adapter = self.rules.bind_to_environ(req.environ)
        res = SolaceResponse()
        try:
            endpoint, values = adapter.match()
            req.params = munch.munchify(values)
            if endpoint not in self.views:
                raise NotFound
            self.views[endpoint](req, res)

            if res.json:
                res.content_type = "application/json"
                res.data = json.dumps(res.json)
            return res
        except HTTPException as e:
            err = {
                'code': e.code,
                'message': e.description
            }
            res = Response(json.dumps({"error": err}), e.code)
            res.content_type = 'application/json'
            return res 
    
    def __wsgi_app(self, environ, start_response):
        req = Request(environ)
        res = self.__dispatch(req)
        return res(environ, start_response)

    def __call__(self, environ, start_response):
        return self.__wsgi_app(environ, start_response)

class DevelopmentServer:
    
    # TODO: look at more configuration options 
    # that we can support for the DevelopmentServer.
    # https://werkzeug.palletsprojects.com/en/2.0.x/serving/

    def __init__(self, app, host, port, debug = True):
        self.app = app
        self.host = host
        self.port = port
        self.debug = debug
    
    def start(self):
        run_simple(
            self.host, 
            self.port, 
            self.app, 
            use_debugger=self.debug, 
            use_reloader=True
        )
