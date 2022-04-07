from http.server import HTTPServer, CGIHTTPRequestHandler, BaseHTTPRequestHandler
import http.server
import socketserver
import urllib

class output(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
   
server_address = ("host", 8010)
server = http.server.HTTPServer(('127.0.0.1', 8010), output)
server.serve_forever()
# from http.server import HTTPServer, BaseHTTPRequestHandler, CGIHTTPRequestHandler

# from io import BytesIO


# class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

#     # определяем метод `do_GET` 
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()
#         self.wfile.write(b'Hello, world!')

#     # определяем метод `do_POST` 
#     def do_POST(self):
#         content_length = int(self.headers['Content-Length'])
#         body = self.rfile.read(content_length)
#         self.send_response(200)
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()
#         response = BytesIO()
#         response.write(b'This is POST request. ')
#         response.write(b'Received: ')
#         response.write(body)
#         self.wfile.write(response.getvalue())

# server_address = ("", 8000)
# httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
# httpd.serve_forever()