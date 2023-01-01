import BaseHTTPServer
import pymavlink

# Create a MAVLink connection object
mav = pymavlink.mavutil.mavlink_connection('udp:0.0.0.0:14550')

# Create a handler for the HTTP server
class Handler(BaseHTTPServer.BaseHTTPRequestHandler):

    # Handle an incoming request
    def do_GET(self):
        # Send a MAVLink message
        mav.mav.heartbeat_send(1, 1, 1, 1, 1)

        # Send an HTTP response
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Hello World!")

# Create an HTTP server and start listening for requests
server = BaseHTTPServer.HTTPServer(('', 8080), Handler)
server.serve_forever()