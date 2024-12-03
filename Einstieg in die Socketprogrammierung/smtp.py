"""
Sends an email using the SMTP protocol.
"""

import socket
import base64
import ssl
import time


def print_info(text: str, end="\n") -> None:
    """
    Prints the given text in blue.

    Args:
        text (str): The text to be printed.

    Returns:
        None
    """
    print(f"\033[94m{text}\033[0m", end=end)


def build_connection() -> socket.socket:
    """
    Builds a connection to the SMTP server.

    Returns:
        socket.socket: The socket object used for communication.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print_info("Connecting to asmtp.htwg-konstanz.de...")
    s.connect(("asmtp.htwg-konstanz.de", 587))
    print_info("Connected to asmtp.htwg-konstanz.de.")
    print_info("Sending EHLO...")
    s.send(b"EHLO asmtp.htwg-konstanz.de\r\n")
    print(s.recv(1024).decode("utf-8"))
    print_info("Starting TLS...")
    s.send(b"STARTTLS\r\n")
    print(s.recv(1024).decode("utf-8"))
    print_info("Socket done.")
    time.sleep(1)
    return s


def send_email(
    s: socket.socket,
    username: str,
    password: str,
    sender: str,
    recipient: str,
    subject: str,
    body: str,
) -> None:
    """
    Sends an email using the given socket.

    Args:
        s (socket.socket): The socket object used for communication.
        username (str): The username used to authenticate with the SMTP server.
        password (str): The password used to authenticate with the SMTP server.
        sender (str): The email address of the sender.
        recipient (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The body of the email.

    Returns:
        None
    """
    print_info("auth login")
    s.send(b"auth login\r\n")
    print(s.recv(1024).decode("utf-8"))
    print_info("username")
    s.send(base64.b64encode(username.encode("utf-8")) + b"\r\n")
    print(s.recv(1024).decode("utf-8"))
    print_info("password")
    s.send(base64.b64encode(password.encode("utf-8")) + b"\r\n")
    print(s.recv(1024).decode("utf-8"))
    print_info("mail from")
    s.send(b"mail from: " + sender.encode("utf-8") + b"\r\n")
    print(s.recv(1024).decode("utf-8"))
    print_info("rcpt to")
    s.send(b"rcpt to: " + recipient.encode("utf-8") + b"\r\n")
    print(s.recv(1024).decode("utf-8"))
    print_info("data")
    s.send(b"data\r\n")
    print(s.recv(1024).decode("utf-8"))
    print_info("sending email")
    s.send(b"from: " + sender.encode("utf-8") + b"\r\n")
    s.send(b"to: " + recipient.encode("utf-8") + b"\r\n")
    s.send(b"subject: " + subject.encode("utf-8") + b"\r\n")
    s.send(
        b"date: " + time.strftime("%a, %d %b %Y %H:%M:%S %z").encode("utf-8") + b"\r\n"
    )
    s.send(b"\r\n")
    s.send(body.encode("utf-8") + b"\r\n.\r\n")
    print(s.recv(1024).decode("utf-8"))
    print_info("quit")
    s.send(b"quit\r\n")
    print(s.recv(1024).decode("utf-8"))


if __name__ == "__main__":
    sock = build_connection()
    print_info("Wrapping socket...")
    context = ssl.create_default_context()
    try:
        ssl_socket = context.wrap_socket(
            sock,
            server_hostname="asmtp.htwg-konstanz.de",
            do_handshake_on_connect=True,
        )
        print_info("Socket wrapped.")
        send_email(
            ssl_socket,
            "fa681wol",
            "password",
            "fa681wol@htwg-konstanz.de",
            "f99wolter@gmail.com",
            "Test",
            "This is a test email.",
        )
    except ssl.SSLError as e:
        print_info("\nSSL Error:\t", end="")
        print(f"{e}")
        print(f"Error number:\t{e.errno}")
        print(f"Error library:\t{e.library}")
        print(f"Error reason:\t{e.reason}")
    finally:
        sock.close()
