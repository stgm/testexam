from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        # doet een unbuffered read, werkt misschien niet voor grotere posts
        print(self.rfile.read1())

        # response naar server
        self.wfile.write(bytes("Werkt OK", "utf8"))

with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()
