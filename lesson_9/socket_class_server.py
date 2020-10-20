import socket
import selectors
import time
import threading
import signal
import sys


class Connection(threading.Thread):
    BUF_SIZE = 4096

    def __init__(self, conn, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn = conn

    def run(self):
        self.read()

    def close(self):
        try:
            self.conn.shutdown(socket.SHUT_RDWR)
            self.conn.close()
        except Exception as e:
            print(e)
        finally:
            self.conn = None

    def read(self):
        # time.sleep(10)
        try:
            data = self.conn.recv(Connection.BUF_SIZE)
            if not data:
                self.close()
                return
        except Exception as e:
            print(e)
            self.close()
            return
        else:
            print(str(data))
            self.write()

    def write(self):
        self.conn.sendall(b"hello client")


class ChatSocket:

    def __init__(self, sock=None, selector=None):
        self.port = 12345
        self.selector = selector
        self.threads = list()
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.sock.close()
        for thread in self.threads:
            thread.join()

    def listen(self):
        self.__init_socket()
        self.__register_selectors()

    def __init_socket(self):
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("127.0.0.1", self.port))
        self.sock.setblocking(False)
        self.sock.listen()

    def __register_selectors(self):
        self.selector.register(self.sock, selectors.EVENT_READ, data="accept")

    def accept_connection(self, key, mask):
        conn, addr = self.sock.accept()
        print(f"Accepted connection from {addr}")
        thread = Connection(conn, daemon=True)
        self.threads.append(thread)
        thread.start()


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
                for key, mask in events:
                    if(key.data == "accept"):
                        chatSocket.accept_connection(key, mask)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
