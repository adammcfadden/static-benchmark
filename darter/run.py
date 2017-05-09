import SocketServer, BaseHTTPServer, SimpleHTTPServer
import ssl, os, sys

port = int(sys.argv[1]) if len(sys.argv) > 1 else 4443
cwd = os.path.dirname(os.path.realpath(__file__))
pem = os.path.join( cwd, 'mycert.pem' )
os.chdir(cwd)

class ThreadingSimpleServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
    pass

class MyHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()
        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("Cache-Control", "public, max-age=6000")

httpd = ThreadingSimpleServer(('0.0.0.0', port), MyHTTPRequestHandler)
# httpd.socket = ssl.wrap_socket(httpd.socket, certfile=pem, server_side=True)
print 'python server watching {} listening on {}'.format(cwd, port)
httpd.serve_forever();
