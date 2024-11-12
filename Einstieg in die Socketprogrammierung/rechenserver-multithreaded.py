import socket
import threading
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

def listen(sock: socket):
    sock.bind((IP, PORT))
    sock.listen(16)
    while True:
        thread = threading.Thread(target=recieve, args=(sock.accept(),))
        thread.start()
    
def recieve(conn: socket.socket):
    (c, addr) = conn
    print("Connection from", addr)
    msg = c.recv(1024)
    if not msg:
        return
    print(f"Received: {msg}")
    (id, op, n) = decode_message(msg)
    result = struct.pack("!Ii", id, calc(op, n))
    c.send(result)
    print(f"Sent: {result}")
    print("Connection closed with", addr)
    c.close()



if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen(sock)