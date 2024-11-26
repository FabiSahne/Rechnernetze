"""
Socket Exercise
"""

import socket

socket.setdefaulttimeout(30)

MY_IP = "127.0.0.2"
MY_PORT = 12345
REMOTE_IP = "127.0.0.1"
REMOTE_PORT = 12345


def start_task(s, msg):
    """
    Sends a message through the given socket and receives a response.

    Args:
        sock (socket.socket): The socket object used for communication.
        msg (str): The message to be sent through the socket.

    Returns:
        None
    """
    s.send(msg.encode("utf-8"))
    msg = s.recv(1024)
    s.close()


def start_server():
    """
    Starts a TCP server that listens for incoming connections.

    The server binds to the IP address and port specified by the global
    variables `MY_IP` and `MY_PORT`. It listens for incoming connections
    and accepts one connection. Upon accepting a connection, it starts
    a task with the connected socket and sends a welcome message.

    If a socket timeout occurs, it is silently ignored.

    Raises:
        socket.error: If an error occurs while creating, binding, or
                      listening on the socket.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((MY_IP, MY_PORT))
    s.listen(1)
    try:
        conn, _ = s.accept()
        start_task(conn, "Thx for connecting!!!")
    except socket.timeout:
        pass


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((REMOTE_IP, REMOTE_PORT))
    start_task(sock, "Thx, for accepting!!!")
except socket.error:
    start_server()
