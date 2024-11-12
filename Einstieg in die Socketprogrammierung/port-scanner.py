import socket
import threading

protocol = None

def scan_port_tcp(ip: str, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        print(f"Port {port} is open")
    except socket.timeout:
        print(f"Port {port}: no response")
    except socket.error:
        print(f"Port {port}: error")
    finally:
        s.close()

def scan_port_udp(ip: str, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)
    s.sendto(b"", (ip, port))
    try:
        s.recvfrom(1024)
        print(f"Port {port} is open")
    except socket.timeout:
        print(f"Port {port}: no response")
    except socket.error:
        print(f"Port {port}: error")
    finally:
        s.close()

def scan(ip: str, ports: list[int]):
    threads = []
    for port in ports:
        thread = None
        if protocol == "TCP":
            thread = threading.Thread(target=scan_port_tcp, args=(ip, port))
        else:
            thread = threading.Thread(target=scan_port_udp, args=(ip, port))
        thread.start()
        threads.append(thread)
    while threads:
        threads.pop().join()

if __name__ == "__main__":
    print("1. UDP, 2. TCP")
    proto = input("Choose protocol: ")
    if proto == "1":
        protocol = "UDP"
    elif proto == "2":
        protocol = "TCP"
    else:
        raise ValueError("Unknown protocol")
    print("Enter IP address")
    ip = input()
    print("Enter starting port")
    port_start = input()
    print("Enter ending port")
    port_end = input()
    ports = range(int(port_start), int(port_end) + 1)
    scan(ip, ports)