# Zu 3.2 Frage 5
# Kann man einen Server betreiben, der Echo-Anfragen auf dem gleichen Port sowohl über UDP als auch über TCP beantwortet?
# Antwort: Nein, es folgt der Fehler: "OSError: [WinError 10048] Only one usage of each socket address (protocol/network address/port) is normally permitted"
import socket
import threading

IP = "localhost"
PORT = 12345

def udp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((IP, PORT))
    print("UDP Server is running on", s.getsockname()[0], s.getsockname()[1])
    while True:
        (msg, addr) = s.recvfrom(1024)
        if not msg:
            break
        print(f"Connection from {addr}")
        print(f"Received: {msg}")
        s.sendto(msg, addr)

def tcp():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, PORT))
    s.listen(5)
    print("TCP Server is running on", s.getsockname()[0], s.getsockname()[1])
    while True:
        (c, addr) = s.accept()
        msg = c.recv(1024)
        if not msg:
            break
        print(f"Connection from {addr}")
        print(f"Received: {msg}")
        c.send(msg)
        c.close()

def start_threads():
    t1 = threading.Thread(target=udp)
    t2 = threading.Thread(target=tcp)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    start_threads()