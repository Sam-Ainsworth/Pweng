from http.server import BaseHTTPRequestHandler, HTTPServer

controllers = {}

class PwengServer(BaseHTTPRequestHandler):

    def do_GET(self):
        routeArr = self.path.split("/")
        routeArr = list(filter(None, routeArr))

        controller = ""
        action = ""

        if len(routeArr) == 0:
            controller = "Main"
            action = "Index"
        elif len(routeArr) == 1:
            controller = routeArr[0]
            action = "Index"
        else:
            controller = routeArr[0]
            action = routeArr[1].split("?")[0] if "?" in routeArr[1] else routeArr[1]

        global controllers;

        controller = controller.lower()
        action = action.lower()

        if controller in controllers:
            if action in controllers[controller]:
                return getPageContent(self, controller, action)
            else:
                return r404(self)
        else:
            return r404(self)
        
    def do_POST(self):
        if self.path == '/login':
           login(self)

def start_server(host,port, c):
    global controllers;
    controllers = c;
    pwengServer = HTTPServer((host, int(port)), PwengServer)
    print("\nPweng Server Running")
    pwengServer.serve_forever()

def r404(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    self.wfile.write("<html><body><h1>404 Not Found</h1></body></html>".encode())

def getPageContent(self, controller, action):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    self.wfile.write("<html><body><h1>Route Found</h1></body></html>".encode())

