import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "."

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Change working directory to where the HTML file is located
os.chdir(DIRECTORY)

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving FM Radio at http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server.")
    httpd.serve_forever()
