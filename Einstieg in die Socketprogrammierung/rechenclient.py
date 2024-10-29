import socket
import random
import numpy as np
import struct


def calc_client(s: socket):
    # s = socket.socket(socket.AF_INET, socket.)
    if s.type == socket.SOCK_STREAM:
        s.connect(('localhost', 12345))
    # random generated id
    id = random.randint(0, 100)
    # user input for operation
    op_num = input("Choose operation (1. SUM, 2. PRO, 3. MIN, 4. MAX): ")
    op = None
    match op_num:
        case "1": op = b"SUM"
        case "2": op = b"PRO"
        case "3": op = b"MIN"
        case "4": op = b"MAX"
        case _: raise ValueError("Unknown operand")
    # user input for numbers
    n = input("Enter numbers separated by space: ")
    n = np.array(list(map(np.int32, n.split())))
    # encode message
    msg = struct.pack("!I3s", id, op) + n.tobytes()
    if s.type == socket.SOCK_STREAM:
        s.send(msg)
        result = struct.unpack("!Ii", s.recv(1024))
    else:
        s.sendto(msg, ('localhost', 12345))
        result = struct.unpack("!Ii", s.recvfrom(1024)[0])
    if result[0] == id:
        print("Result:", result[1])


if __name__ == "__main__":
    print("1. DGRAM, 2. STREAM")
    sock_type = input("Choose socket type: ")
    s = None
    match sock_type:
        case "1": s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        case "2": s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        case _: raise ValueError("Unknown socket type")
    calc_client(s)