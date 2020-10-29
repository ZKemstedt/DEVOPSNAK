import socket
import selectors
import logging

from server.message import Message

log = logging.getLogger(__name__)
sel = selectors.DefaultSelector()

host = '127.0.0.1'
port = 65432
filepath = 'server/files'


def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    log.info(f'accepted connection from {addr}')
    conn.setblocking(False)
    message = Message(sel, conn, addr, filepath)
    sel.register(conn, selectors.EVENT_READ, data=message)


lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Avoid bind() exception: OSError: [Errno 48] Adress already in use
lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

lsock.bind((host, port))
lsock.listen()
log.info(f'listening on {(host, port)}')
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                message = key.data
                try:
                    message.process_events(mask)
                except Exception as e:
                    log.exception(f'Encountered exception when trying to process events for {message.addr}',
                                  exc_info=e)
                    message.close()
except KeyboardInterrupt:
    log.info('keyboard interrupt, exiting.')
finally:
    sel.close()
