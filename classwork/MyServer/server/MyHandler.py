from http.server import BaseHTTPRequestHandler
import re


_post_dispatch = []
_get_dispatch = []

def post(re_path):
    def real_decorator(function):
        def decorated_function(*args, **kwargs):
            return function(*args, *kwargs)
        disp = ( re.compile(re_path), decorated_function, )
        _post_dispatch.append(disp)
        return decorated_function
    return real_decorator

def get(re_path):
    def real_decorator(function):
        def decorated_function(*args, **kwargs):
            return function(*args, *kwargs)
        disp = ( re.compile(re_path), decorated_function, )
        _get_dispatch.append(disp)
        return decorated_function
    return real_decorator

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        for regexp, function in _get_dispatch:
            M = regexp.match(self.path)
            if not M:
                continue
            params = M.groups()
            function(self, *params)
            return
        self.send_error(404, 'Page not found')
        self.end_headers()

    @get(r'/test/?')
    def test_request(self):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        response_body = 'Все хорошо, прекрасная маркиза'
        resp_data = response_body.encode('utf-8')
        self.wfile.write(resp_data)
 
    @get(r'/clients/quantity/?')
    def clients_count(self):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        N = self.server.clients_count
        response_body = str(N)
        resp_data = response_body.encode('utf-8')
        self.wfile.write(resp_data)

    @get(r'/clients/message/?')
    def total_messages(self):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        N = self.server.messages_count
        response_body = str(N)
        resp_data = response_body.encode('utf-8')
        self.wfile.write(resp_data)

    @get(r'/clients/list/?')
    def clients_list(self):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        response_body = '\n'.join(self.server.all_clients)
        resp_data = response_body.encode('utf-8')
        self.wfile.write(resp_data)

    @get(r'/number/(\d+)/?')
    def number_for(self, client):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        response_body = str(self.server.count_msg_for(client))
        resp_data = response_body.encode('utf-8')
        self.wfile.write(resp_data)
    
    @get(r'/next/(\d+)/?')
    def take_next(self, client):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        response_body = self.server.take_next(client)
        if not response_body:
            response_body = '<no more messages>'
        resp_data = response_body.encode('utf-8')
        self.wfile.write(resp_data)
        
 