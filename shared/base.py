# Heavily based on realpython's guide to python sockets.
# guide: https://realpython.com/python-sockets/#application-client-and-server
# github: https://github.com/realpython/materials/tree/master/python-sockets-tutorial

import sys
import selectors
import struct
import logging

from shared.utils import json_encode, json_decode

log = logging.getLogger(__name__)


class MessageBase(object):

    def __init__(self, selector, sock, addr, files):
        self.files = files
        self.selector = selector
        self.sock = sock
        self.addr = addr
        self._recv_buffer = b''
        self._send_buffer = b''
        self._jsonheader_len = None
        self.jsonheader = None

    # --- core ---

    def _set_selector_events_mask(self, mode):
        """Set selector to listen for events: mode if 'r', 'w', or 'rw'."""
        if mode == 'r':
            events = selectors.EVENT_READ
        elif mode == 'w':
            events = selectors.EVENT_WRITE
        elif mode == 'rw':
            events = selectors.EVENT_READ | selectors.EVENT_WRITE
        else:
            raise ValueError(f'Invalid events mask mode {repr(mode)}.')
        log.debug(f'{self.addr} selector set to listen for \'{mode}\'')
        self.selector.modify(self.sock, events, data=self)

    def process_events(self, mask):
        if mask & selectors.EVENT_READ:
            self.read()
        if mask & selectors.EVENT_WRITE:
            self.write()

    def close(self):
        log.info(f'closing connection to {self.addr}')
        try:
            self.selector.unregister(self.sock)
        except Exception as e:
            log.exception(f'exception when trying to unregister selector for addr {self.addr}.', exc_info=e)

        try:
            self.sock.close()
        except OSError as e:
            log.exception(f'exception when trying to close socket for addr {self.addr}.', exc_info=e)
        finally:
            # delete reference to socket object for garbage collection
            self.sock = None

    def read(self):
        # different for server/client
        raise NotImplementedError('Must be implemented by child class.')

    def write(self):
        # different for server/client
        raise NotImplementedError('Must be implemented by child class.')

    def _read(self):
        try:
            # should be ready to read
            data = self.sock.recv(4096)
        except BlockingIOError:
            # resource temporarily unavailable (errno EWOULDBLOCK)
            pass
        else:
            if data:
                self._recv_buffer += data
            else:
                raise RuntimeError('Peer closed.')

    def _write(self):
        if self._send_buffer:
            log.trace(f'sending {len(self._send_buffer)} bytes of data to {self.addr}')
            try:
                # should be ready to write
                sent = self.sock.send(self._send_buffer)
            except BlockingIOError:
                # resource temporarily unavailable (errno EWOULDBLOCK)
                pass
            else:
                self._send_buffer = self._send_buffer[sent:]

    # --- outbound ---

    def _create_message(self, *, content_bytes, content_type, content_encoding, content_name=None):
        jsonheader = {
            'byteorder': sys.byteorder,
            'content-type': content_type,
            'content-encoding': content_encoding,
            'content-length': len(content_bytes),
            'content-name': content_name,
        }
        jsonheader_bytes = json_encode(jsonheader, 'utf-8')
        messageheader = struct.pack('>H', len(jsonheader_bytes))
        message = messageheader + jsonheader_bytes + content_bytes
        return message

    # --- inbound ---

    def process_protoheader(self):
        hdrlen = 2
        if len(self._recv_buffer) >= hdrlen:
            self._jsonheader_len = struct.unpack('>H', self._recv_buffer[:hdrlen])[0]
            self._recv_buffer = self._recv_buffer[hdrlen:]

    def process_jsonheader(self):
        hdrlen = self._jsonheader_len
        if len(self._recv_buffer) >= hdrlen:
            self.jsonheader = json_decode(self._recv_buffer[:hdrlen], 'utf-8')
            self._recv_buffer = self._recv_buffer[hdrlen:]

            for req in ['byteorder', 'content-length', 'content-type', 'content-encoding']:
                if req not in self.jsonheader:
                    raise ValueError(f'Missing required header "{req}".')

    def process_incoming_message(self):
        # 1. read message from buffer
        content_len = self.jsonheader['content-length']
        if not len(self._recv_buffer) >= content_len:
            return
        data = self._recv_buffer[:content_len]
        self._recv_buffer = self._recv_buffer[content_len:]

        # 2. if json, decode it.
        content_type = self.jsonheader['content-type']
        if content_type == 'text/json':
            data = json_decode(data, self.jsonheader['content-encoding'])
        log.trace(f'received {content_type} ({content_len}) from {self.addr}')

        self.handle_message(data)

    def handle_message(self, data):
        # different for server/client
        raise NotImplementedError('must be implemented by child class.')
