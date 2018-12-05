from http.server import BaseHTTPRequestHandler, HTTPServer
class PwengServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/login':
            do_login(self)
    def do_POST(self):
        if self.path == '/login':
           login(self)

def start_server(host,port):
    pwengServer = HTTPServer((host, int(port)), PwengServer)
    print("\nPweng Server Running")
    pwengServer.serve_forever()
