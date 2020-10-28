# Heavily based on realpython's guide to python sockets.
# guide: https://realpython.com/python-sockets/#application-client-and-server
# github: https://github.com/realpython/materials/tree/master/python-sockets-tutorial

import sys
import selectors
import json
import io
import struct
import logging

log = logging.getLogger(__name__)


class MessageBase(object):

    def __init(self, selector, sock, addr):
        self.selector = selector
        self.sock = sock
        self.addr = addr
        self._recv_buffer = b''
        self._send_buffer = b''
        self.jsonheader_len = None
        self.jsonheader = None

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

    def _read(self):
        try:
            # Should be ready to read
            data = self.sock.recv(4096)
        except BlockingIOError:
            # Resource temporarily unavailable (errno EWOULDBLOCK)
            pass
        else:
            if data:
                log.trace(f'receiving {repr(data)} from {self.addr}')
                self._recv_buffer += data
            else:
                raise RuntimeError('Peer closed.')  # TODO

    def _write(self):
        if self._send_buffer:
            log.trace(f'sending {repr(self._send_buffer)} to {self.addr}')
            try:
                # Should be ready to write
                sent = self.sock.send(self._send_buffer)
            except BlockingIOError:
                # Resource temporarily unavailable (errno EWOULDBLOCK)
                pass
            else:
                self._send_buffer = self._send_buffer[sent:]

    def _json_encode(self, obj, encoding):
        return json.dumps(obj, ensure_ascii=False).encode(encoding)

    def _json_decode(self, json_bytes, encoding):
        with io.TextIOWrapper(io.BytesIO(json_bytes), encoding=encoding, newline='') as tiow:
            obj = json.load(tiow)
        return obj

    def _create_message(self, *, content_bytes, content_type, content_encoding):
        jsonheader = {
            'byteorder': sys.byteorder,
            'content-type': content_type,
            'content-encoding': content_encoding,
            'content-length': len(content_bytes),
        }
        jsonheader_bytes = self._json_encode(jsonheader, 'utf-8')
        messageheader = struct.pack('>H', len(jsonheader_bytes))
        message = messageheader + jsonheader_bytes + content_bytes
        return message

    def process_events(self, mask):
        if mask & selectors.EVENT_READ:
            self.read()
        if mask & selectors.EVENT_WRITE:
            self.write()

    def read(self):
        raise NotImplementedError('Must be implemented by child class.')

    def write(self):
        raise NotImplementedError('Must be implemented by child class.')

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
            # Delete reference to socket object for garbage collection
            self.sock = None

    def process_protoheader(self):
        hdrlen = 2
        if len(self._recv_buffer) >= hdrlen:
            self.jsonheader_len = struct.unpack('>H', self._recv_buffer[hdrlen:])[0]
            self._recv_buffer = self._recv_buffer[hdrlen:]

    def process_jsonheader(self):
        hdrlen = self.jsonheader_len
        if len(self._recv_buffer) >= hdrlen:
            self.jsonheader = self._json_decode(self._recv_buffer[:hdrlen], 'utf-8')
            self._recv_buffer = self._recv_buffer[hdrlen]

            for req in ['byteorder', 'content-length', 'content-type', 'content-encoding']:
                if req not in self.jsonheader:
                    raise ValueError(f'Missing required header "{req}".')

    def process_incoming_message(self):
        """
        Process the incoming message by reading `content-len` from the buffer.
        If the `content-type` is json, decode it.
        When done, set the selector to listen to write events.
        """
        content_len = self.jsonheader['content-length']
        if not len(self._recv_buffer) >= content_len:
            return
        data = self._recv_buffer[:content_len]
        self._recv_buffer = self._recv_buffer[content_len:]

        _type = self.jsonheader['content-type']
        if _type == 'text/json':
            # content type is json
            encoding = self.jsonheader['content-encoding']
            self.request = self._json_decode(data, encoding)
            log.info(f'received request {repr(self.request)} from {self.addr}')
        else:
            # content type is binary (or unknown)
            self.request = data
            log.info(f'received {_type} request from {self.addr}')

        # set selector to listen for write events, we're done reading.
        self._set_selector_events_mask('w')
