from django.db import models
from http.server import BaseHTTPRequestHandler

# Create your models here.

class Contact(models.Model):
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=122)

    def __str__(self) -> str:
          return self.username


class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return



