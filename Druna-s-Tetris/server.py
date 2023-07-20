import http.server
import socketserver
import threading
import webbrowser
import subprocess

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/start_server':
            # Start the game server in a separate process
            subprocess.Popen(['py', 'main.py'])

            # Send a response to indicate the server has started successfully
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')  # Add the CORS header here
            self.end_headers()
            self.wfile.write(b'Server started successfully!')

        # Serve the game files
        else:
            self.send_response(404)
            self.send_header('Access-Control-Allow-Origin', '*')  # Add the CORS header here
            super().do_GET()

# Start the HTTP server
with socketserver.TCPServer(("", 8888), MyHandler) as httpd:
    print("Server started on port 8888")
    threading.Thread(target=httpd.serve_forever).start()

    # Optionally, open the game client in a web browser
    webbrowser.open('http://localhost:8888')

    # Wait for the server to finish
    httpd.serve_forever()
