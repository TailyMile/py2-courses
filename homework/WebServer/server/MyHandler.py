import os
from http.server import BaseHTTPRequestHandler
import re
import logging

_post_dispatch = []
_get_dispatch = []

def post(re_path):
    def real_decorator(function):
        def decorated_function(*args, **kwargs):
            return function(*args, **kwargs)
        disp = (re.compile(re_path), decorated_function)
        _post_dispatch.append(disp)
        return decorated_function
    return real_decorator

def get(re_path):
    def real_decorator(function):
        def decorated_function(*args, **kwargs):
            return function(*args, **kwargs)
        disp = (re.compile(re_path), decorated_function)
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

    def do_POST(self):
        for regexp, function in _post_dispatch:
            M = regexp.match(self.path)
            if not M:
                continue
            params = M.groups()
            function(self, *params)
            return
        self.send_error(404, 'Page not found')
        self.end_headers()

    @post(r'/message_to/(\d+)/?')
    def recv_message(self, client):
        size = int(self.headers['Content-length'])
        message = self.rfile.read(size).decode('utf-8')
        self.server.message_to(client, message)
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        response_body = 'OK'
        resp_data = response_body.encode('utf-8')
        self.wfile.write(resp_data)

    @post(r'/upload/(\d+)/?')  # Новый маршрут для загрузки файла
    def upload_file(self, client):
        content_length = int(self.headers['Content-Length'])
        file_data = self.rfile.read(content_length)

        # Сохраняем файл с уникальным именем
        client_folder = 'uploaded_files'  # Папка для всех файлов
        if not os.path.exists(client_folder):
            os.makedirs(client_folder)

        # Генерируем имя файла
        file_name = f"{client}-{len(os.listdir(client_folder)) + 1}.bin"
        file_path = os.path.join(client_folder, file_name)

        with open(file_path, 'wb') as f:
            f.write(file_data)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(f'File uploaded as {file_name}'.encode('utf-8'))