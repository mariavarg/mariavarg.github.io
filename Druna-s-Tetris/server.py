import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/start_server':
            # Start the Python server
            try:
                with socketserver.TCPServer(("", 8000), http.server.SimpleHTTPRequestHandler) as httpd:
                    print("Server started on port 8000")
                    httpd.serve_forever()
            except OSError as e:
                print(f"Failed to start the server: {e}")
                self.send_response(500)
                self.end_headers()
                self.wfile.write(bytes(f"Failed to start the server: {e}", "utf-8"))
                return

        # Handle other requests if needed
        else:
            super().do_GET()

# Start the server
if __name__ == "__main__":
    with socketserver.TCPServer(("", 8080), MyHandler) as httpd:
        print("Server started on port 8080")
        httpd.serve_forever()
