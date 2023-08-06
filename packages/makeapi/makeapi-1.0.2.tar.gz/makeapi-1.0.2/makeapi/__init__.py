from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import urllib.parse
from urllib.parse import parse_qs
import typing
import json

__version__ = "1.0.2"

def render_template(file):
    if file != None:
        with open("templates/" + file, "r") as f:
            data = f.read()
        return {"html": data, "content-type": "text/html"} 

def textresp(data : str):
#    data = data.replace("\n", "<br>")
    data = f"<!DOCTYPE html><html><body><h2>{data}</h2></body></html>"
    return {"html": data, "content-type": "text/html"} 

def htmlresp(data : str):
    return {"html": data, "content-type": "text/html"} 

def jsonresp(data : dict):
    data = f"<!DOCTYPE html><html><body><pre><code>{data}</code></pre></body></html>"
    return {"json": data, "content-type": "application/json"}  

class Request:
    def __init__(self, args):
        self.args = args 

class MakeAPI():
    def __init__(self, server_address, server_port, handler_class):
        self.server_address = server_address
        self.server_port = server_port
        self.handler = handler_class
        self.handler.routes = []
                                                             
    def get(self,route):
        
        def decorator(f : typing.Callable, *args, **kwargs) -> typing.Callable:              
            self.handler.routes.append((route, f))
        return decorator
                                                   
    def run(self):
        server_address = (self.server_address, self.server_port)
        httpd = HTTPServer(server_address, self.handler)
        print("* Running on http://{}:{}/ (CTRL+C to quit)".format(self.server_address, self.server_port))
        print("* Endpoints:")
        for route, func in self.handler.routes:
            print(f"    * {route}")
        httpd.serve_forever()

                                  
class MakeAPIRequest(BaseHTTPRequestHandler):
                   
      
                        
    def do_GET(self):
        for route, fn in self.routes:
            if "?" in self.path:
                r = [route]
                p_list = self.path.split("?")
            else:
                p_list = [self.path] 
                r = [route]        
            if p_list[0] == r[0]:
                args = parse_qs(urllib.parse.urlparse(self.path).query)  
               
                func = fn(request=Request(args=args))
                self.send_response(200)
                self.send_header("Content-type", func["content-type"])
                self.end_headers()
                try:
                    func["json"]
                except KeyError:
                    self.wfile.write(bytes(func["html"],"utf-8"))
                else:
                    self.wfile.write(bytes(func["json"], "utf-8"))                        