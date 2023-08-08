import http.server
import socketserver
import webbrowser
import subprocess
import json

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            super().do_GET()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        post_data = json.loads(post_data)

        if 'action' in post_data and post_data['action'] == 'start_server':
            subprocess.Popen(['python', 'main.py'])  # Use 'python' instead of 'py' for Windows

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {'message': 'Server started successfully!'}
            self.wfile.write(json.dumps(response).encode('utf-8'))

            # Optionally, open the game client in a web browser
            webbrowser.open('http://localhost:8443')

        else:
            self.send_response(400)
            self.send_header('Access-Control-Allow-Origin', '*')
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
