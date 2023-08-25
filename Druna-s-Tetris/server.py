import http.server
import socketserver
import webbrowser
import subprocess
import pygame
import json
import os  # Import the 'os' module to work with file paths

# Define the directory where your files are located
file_directory = 'favicon_package_v0.16'

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def do_POST(self):
        if self.path == '/start_server':
            # Start the game server in a separate process
            subprocess.Popen(['python', 'project.py'])  # Use 'python' instead of 'py' for Windows

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
            
        # Serve the favicon and other resources
        if self.path.startswith('/favicon_package_v0.16'):
            # Get the requested file path within the folder
            file_path = self.path[1:]  # Remove the leading '/'
            full_file_path = os.path.join(file_directory, file_path)

            if os.path.exists(full_file_path):
                # Load and serve the requested file
                with open(full_file_path, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'image/png')  # Adjust the content type if needed
                self.end_headers()
                self.wfile.write(content)
            else:
                # If the file doesn't exist, return a 404 response
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'File not found')
    
# Start the HTTP server
with socketserver.TCPServer(("", 8443), MyHandler) as httpd:  # Listen on port 8443
    print("Server started on port 8443")

    # Keep the server running until interrupted
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

print("Server stopped.")
