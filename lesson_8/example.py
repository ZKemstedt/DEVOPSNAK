import socket

# Return the true host name, a list of aliases,
# and a list of IP addresses, for a host.
print(socket.gethostbyname_ex(socket.gethostname()))


"""
Running an example several times with too small delay between executions, could lead to this error:

OSError: [Errno 98] Address already in use
This is because the previous execution has left the socket in a TIME_WAIT state, and can’t be immediately reused.

There is a socket flag to set, in order to prevent this, socket.SO_REUSEADDR:
"""
HOST = "127.0.0.1"
PORT = 7777
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.close()
