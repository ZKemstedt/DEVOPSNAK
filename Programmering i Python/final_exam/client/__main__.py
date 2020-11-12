import os
import sys
import fcntl
import socket
import threading
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

aliases = {
    'ls': 'list-files',
    'get': 'get-file',
    'send': 'send-file',
    'rm': 'remove-file',
}

help_commands = (
            ' --- commands ---\n'
            'quit\n'
            '?\n'
            'list-files\n'
            'get-file <filename>\n'
            'send-file <filename>\n'
            'remove-file <filename>\n'
        )


# https://stackoverflow.com/questions/21791621/taking-input-from-sys-stdin-non-blocking
def set_input_nonblocking():
    orig_fl = fcntl.fcntl(sys.stdin, fcntl.F_GETFL)
    fcntl.fcntl(sys.stdin, fcntl.F_SETFL, orig_fl | os.O_NONBLOCK)


def from_keyboard(arg1, arg2):
    line = arg1.read().rstrip('\n')

    if not line:
        return

    elif line == 'quit':
        raise KeyboardInterrupt

    elif line == '?':
        print(help_commands)

    elif line == 'ls local' or line == 'local':
        print(filemanager.list_files())

    else:
        args = line.split()
        action = aliases.get(args.pop(0), None)
        if not action:
            print('invalid action')
            return

        if args:
            value = ''.join(args)
        else:
            value = None
        start_connection(host, port, action, value)


def start_connection(host, port, action, value):
    addr = (host, port)
    log.info(f'starting connection to {addr}')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    message = Message(sel, sock, addr, filemanager, action, value)
    sel.register(sock, events, data=message)


def sync_clock(wait, func):
    global sync
    sync = threading.Timer(interval=wait, function=func)
    sync.start()


def sync_get_remote():
    action = 'request-register'
    value = None
    start_connection(host, port, action, value)
    sync_clock(wait=2, func=sync_compare_and_fetch)


def sync_compare_and_fetch():
    filemanager.compare_registers()
    for filename in filemanager.todo:
        action = 'get-file'
        value = filename
        start_connection(host, port, action, value)
        log.info(f'sync: requesting file {filename}')
    sync_clock(wait=30, func=sync_get_remote)


def selector_wrapper(key, mask):
    # socket event
    if isinstance(key.data, Message):
        message = key.data
        try:
            message.process_events(mask)
        except Exception as e:
            log.exception('encountered exception when trying to process events for a socket.', exc_info=e)
            message.close()
    # stdin event
    else:
        callback = key.data
        try:
            callback(key.fileobj, mask)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            log.exception('encountered exception in main loop.', exc_info=e)


set_input_nonblocking()
sel.register(sys.stdin, selectors.EVENT_READ, from_keyboard)

sync = threading.Timer(interval=2, function=sync_clock, args=(0, sync_get_remote))

try:
    sync.start()
    # loops ends by keyboard interrupt.
    # the reason for this is to be able to bail out
    # in case something gets stuck.
    while True:
        sys.stdout.write('>>> ')
        sys.stdout.flush()

        for key, mask in sel.select():
            selector_wrapper(key, mask)

except KeyboardInterrupt:
    log.info('client exit')
finally:
    sync.cancel()
    sel.unregister(sys.stdin)
    sel.close()
