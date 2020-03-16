from http.server import HTTPServer, BaseHTTPRequestHandler
from collections import OrderedDict
import time
import json

class ExpressServer(BaseHTTPRequestHandler):
    def do_GET(self):
        path_parts = self.path.split("/")
        print(path_parts)
        self.send_response_only(404)
        self.end_headers()
        self.wfile.write(json.dumps({"data": "jebac biede"}).encode("utf-8"))

    def do_POST(self):
        if self.headers["Content-Type"] == "application/json":
            content_lenght = int(self.headers["Content-Lenght"])
            paload = self.rfile.read(content_lenght)

            data = json.loads(payload.decode("utf-8"))
            print(data)

            self.send_resonse(201)
            self.end_headers()
            self.wfile.write(b"it works")

if __name__ == '__main__':
    server = HTTPServer(("", 8889), ExpressServer)
    server.serve_forever()


# do odpalenia python nazwa.py

