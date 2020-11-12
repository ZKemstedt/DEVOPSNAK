import socket
import struct

HOST = "127.0.0.1"
PORT = 12345

DATA_TYPE = {
    "text": b"0",
    "image": b"1"
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = b"hello world"
    header = struct.pack("!Lc", len(message), b"0")
    s.sendall(header)
    s.sendall(message)
