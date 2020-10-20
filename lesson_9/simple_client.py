import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"hello server")

    data = s.recv(4096)
    if data:
        print(data.decode())
