import socket
import selectors
import signal
import sys
import time


class Connection:
    BUF_SIZE = 4096

    def __init__(self, conn, selector):
        self.conn = conn
        self.selector = selector
        self.status = "CLOSED"
        self.incoming = []
        self.outgoing = []

    def activate(self, conn_id):
        self.__register_selectors(self.conn, events=selectors.EVENT_READ | selectors.EVENT_WRITE, data=conn_id)

    def __register_selectors(self, fileobj, events=selectors.EVENT_READ, data=None):
        self.selector.register(fileobj, events, data)

    def close(self):
        self.selector.unregister(self.conn)

    def read(self):
        try:
            data = self.conn.recv(Connection.BUF_SIZE)
            if data == b'':
                self.close()
                return
            if(data):
                self.incoming.append(data)
                self.outgoing.append(data)

        except Exception as e:
            print(e)
            self.close()
            return
        else:
            print(str(data))
            self.write()

    def write(self):
        try:
            if(len(self.outgoing)):
                self.conn.sendall(self.outgoing.pop())

        except Exception as e:
            print(e)


class ChatSocket:

    def __init__(self, sock=None, selector=None):
        self.port = 12345
        self.selector = selector
        self.connections = dict()
        self.threads = list()
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connection_read(self, conn_id):
        self.connections[conn_id].read()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.selector.unregister(self.sock)
        self.sock.close()

    def listen(self):
        self.__init_socket()
        self.__register_selectors(self.sock, data="accept")

    def __init_socket(self):
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("127.0.0.1", self.port))
        self.sock.setblocking(False)
        self.sock.listen()

    def __register_selectors(self, fileobj, events=selectors.EVENT_READ, data=None):
        self.selector.register(fileobj, events, data)

    def handle_connection(self, conn):
        conn.setblocking(False)
        connection = Connection(conn, self.selector)
        conn_id = f"conn:{id(connection)}"
        self.connections[conn_id] = connection
        connection.activate(conn_id)

    def accept_connection(self, key, mask):
        conn, addr = self.sock.accept()
        print(f"Accepted connection from {addr}")
        self.handle_connection(conn)


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)


def setup_signal_handler():
    signal.signal(signal.SIGINT, signal_handler)


def main():
    setup_signal_handler()
    sel = selectors.DefaultSelector()
    with ChatSocket(selector=sel) as chatSocket:
        chatSocket.listen()

        try:
            while True:
                events = sel.select(timeout=1.0)
                time.sleep(1)
                for key, mask in events:
                    if(key.data == "accept"):
                        chatSocket.accept_connection(key, mask)
                    if(key.data.startswith("conn:") and mask & selectors.EVENT_READ):
                        print(f"hello {key.data}")
                        chatSocket.connection_read(key.data)
                    if(mask & selectors.EVENT_WRITE):
                        print("event_write")

        except Exception as e:
            print("end program")
            print(e)


if __name__ == "__main__":
    main()
