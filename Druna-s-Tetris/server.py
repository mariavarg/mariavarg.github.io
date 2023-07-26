import http.server
import socketserver
import webbrowser
import subprocess
import time

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/start_server':
            # Start the game server in a separate process
            subprocess.Popen(['python', 'main.py'])  # Use 'python' instead of 'py' for Windows

            # Wait for the game server to start (adjust the delay as needed)
            time.sleep(2)

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
with socketserver.TCPServer(("", 443), MyHandler) as httpd:  # Listen on port 443
    print("Server started on port 443")

    # Optionally, open the game client in a web browser
    webbrowser.open('http://localhost:443')

    print("Server started on port 888")

    # Optionally, open the game client in a web browser
    webbrowser.open('http://localhost:888')

 # Keep the server running until interrupted
    httpd.serve_forever()
    

