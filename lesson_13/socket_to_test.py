import socket


def send_message(client, send_msg):
    bytes_msg = send_msg.encode()
    client.send(bytes_msg)


def open_connection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 12345))
    return sock


def main():
    client = open_connection()
    send_message(client, "hello world")


if __name__ == "__main__":
    main()
