import socket
import selectors
import logging

from client.message import Message

log = logging.getLogger(__name__)
sel = selectors.DefaultSelector()

host = '127.0.0.1'
port = 65432
filepath = 'client/files'


def start_connection(host, port, action, value):
    addr = (host, port)
    log.info(f'starting connection to {addr}')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    message = Message(sel, sock, addr, filepath, action, value)
    sel.register(sock, events, data=message)


action = 'get-file'
value = 'wallpaper-2791474.jpg'
start_connection(host, port, action, value)

try:
    while True:
        events = sel.select(timeout=1)
        for key, mask in events:
            message = key.data
            try:
                message.process_events(mask)
            except Exception as e:
                log.exception('encountered exception when trying to process events.', exc_info=e)
                message.close()
        # Check for a socket being monitored to continue.
        if not sel.get_map():
            break
except KeyboardInterrupt:
    log.info('keyboard interrupt, exiting.')
finally:
    sel.close()
