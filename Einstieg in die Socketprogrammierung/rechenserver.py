import socket
import numpy as np
import struct

IP = "localhost"
PORT = 12345


def decode_message(msg: bytes) -> tuple[int, bytes, np.array]:
    # (id, op) = struct.unpack("!I3s", msg[0:7])
    id = int.from_bytes(msg[0:4])
    op = msg[4:7]
    size = struct.unpack("!B", msg[7:8])[0]
    last = 8 + size * 4
    n = np.frombuffer(msg[8:last], dtype=np.int32)
    return (id, op, n)

def calc(op: bytes, n: np.array) -> int:
    match op:
        case b"SUM": return np.sum(n)
        case b"PRO": return np.prod(n)
        case b"MIN": return np.min(n)
        case b"MAX": return np.max(n)

def start_server(s):
    print("Starting server")
    s.bind((IP, PORT))
    if s.type == socket.SOCK_STREAM:
        s.listen(5)
    serve(s)

def serve(s: socket):
    print("Server is running on", s.getsockname()[0], s.getsockname()[1])
    while True:
        if s.type == socket.SOCK_STREAM:
            (c, addr) = s.accept()
            msg = c.recv(1024)
        else:
            (msg, addr) = s.recvfrom(1024)
        if not msg:
            break
        print(f"Connection from {addr}")
        print(f"Received: {msg}")
        (id, op, n) = decode_message(msg)
        result = struct.pack("!Ii", id, calc(op, n))
        if s.type == socket.SOCK_STREAM:
            c.send(result)
            c.close()
        else:
            s.sendto(result, addr)

if __name__ == "__main__":
    print("1. UDP, 2. TCP")
    sock_type = input("Choose socket type: ")
    s = None
    match sock_type:
        case "1": s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        case "2": s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        case _: raise ValueError("Unknown socket type")
    start_server(s)