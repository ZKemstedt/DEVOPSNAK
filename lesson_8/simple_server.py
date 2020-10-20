import socket
import struct

BUF_SIZE = 4096

# Context manager
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 12345))
    s.listen()

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            header = conn.recv(5)
            msg_len, data = struct.unpack('!Lc', header)
            data = b''
            while len(data) < msg_len:
                data += conn.recv(BUF_SIZE)
            print(data)
