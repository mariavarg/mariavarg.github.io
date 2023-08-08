import http.server
import socketserver
import webbrowser
import subprocess
import json

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/start_server':
            # Start the game server in a separate process
            subprocess.Popen(['python', 'main.py'])  # Use 'python' instead of 'py' for Windows

            # Send a response to indicate the server has started successfully
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')  # Add the CORS header here
            self.end_headers()
            self.wfile.write(b'Server started successfully!')

        else:
            self.send_response(404)
            self.send_header('Access-Control-Allow-Origin', '*')  # Add the CORS header here
            self.end_headers()

    
# Start the HTTP server
with socketserver.TCPServer(("", 8443), MyHandler) as httpd:  # Listen on port 8443
    print("Server started on port 8443")

    # Keep the server running until interrupted
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

print("Server stopped.")
