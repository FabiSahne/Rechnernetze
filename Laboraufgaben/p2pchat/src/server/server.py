"""P2P Server"""
import socket

class Server:
    """
    Initializes server with given *address* (a 2-tuple (host, port))

    >>> serv = Server(('', 8080))
    ... serv.serve()
    """
    def __init__(self, address):
        self.sock = socket.create_server(address)

    def serve(self):
        while True:
            conn, addr = self.sock.accept()
            # handle new connection

if __name__ == "__main__":
    server = Server(('', 8080))
    server.serve()
