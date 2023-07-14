import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/start_server':
            # Start the game server
            start_game()

            # Send a response to indicate the server has started successfully
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Server started successfully!')

        # Serve the game files
        else:
            super().do_GET()

def start_game():
    import pygame
    import random

    pygame.init()

    # Rest of the game logic goes here...

# Start the server
if __name__ == "__main__":
    with socketserver.TCPServer(("", 8080), MyHandler) as httpd:
        print("Server started on port 8080")
        httpd.serve_forever()

     
