# https://realpython.com/python-sockets/

import socket
import sys

# AF_INET = ipv4
# AF_INET6 = ipv6
# SOCK_STREAM = tcp
# SOCK_QGRAM = udp

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created.")
except socket.error as err:
    print(f"Socket creation failed with error {err}")

# default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    # this means could not resolve the host.
    print('There was an error resolving the host.')
    sys.exit()

# connecting to the server
s.connect((host_ip, port))

print(f"The socket succesfully connected to google ({host_ip})")
