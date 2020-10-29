import os
import sys
import fcntl
import socket
import selectors
import logging

from client.message import Message
from shared.filemanager import FileManager

log = logging.getLogger(__name__)
sel = selectors.DefaultSelector()

host = '127.0.0.1'
port = 65432
filepath = 'client/files'
filemanager = FileManager(filepath)


# https://stackoverflow.com/questions/21791621/taking-input-from-sys-stdin-non-blocking
def set_input_nonblocking():
    orig_fl = fcntl.fcntl(sys.stdin, fcntl.F_GETFL)
    fcntl.fcntl(sys.stdin, fcntl.F_SETFL, orig_fl | os.O_NONBLOCK)


def from_keyboard(arg1, arg2):
    line = arg1.read().rstrip('\n')
    if line == 'quit':
        raise KeyboardInterrupt
    elif line == 'list-files':
        start_connection(host, port, 'list-files', None)
    elif line.startswith('get-file'):
        args = line.split()
        action = args.pop(0)
        value = ''.join(args)
        start_connection(host, port, action, value)
    else:
        log.info(f'user input: {line}')


def start_connection(host, port, action, value):
    addr = (host, port)
    log.info(f'starting connection to {addr}')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    message = Message(sel, sock, addr, filemanager, action, value)
    sel.register(sock, events, data=message)


set_input_nonblocking()
sel.register(sys.stdin, selectors.EVENT_READ, from_keyboard)

try:
    # loops ends by keyboard interrupt.
    # the reason for this is to be able to bail out
    # in case something gets stuck.
    while True:
        sys.stdout.write('>>> ')
        sys.stdout.flush()

        for key, mask in sel.select():
            if isinstance(key.data, Message):
                message = key.data
                try:
                    message.process_events(mask)
                except Exception as e:
                    log.exception('encountered exception when trying to process events for a socket.', exc_info=e)
                    message.close()
            else:
                callback = key.data
                try:
                    callback(key.fileobj, mask)
                except KeyboardInterrupt:
                    raise
                except Exception as e:
                    log.exception('encountered exception in main loop.', exc_info=e)

except KeyboardInterrupt:
    log.info('Closing client.')
finally:
    sel.unregister(sys.stdin)
    sel.close()
