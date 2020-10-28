import logging

from shared.base import MessageBase
from shared.utils import json_encode

log = logging.getLogger(__name__)


class Message(MessageBase):

    # --- overrides ---

    def __init__(self, selector, sock, addr, files):
        super().__init__(selector, sock, addr)
        self.files = files
        self.request = None
        self.response_created = False

    def read(self):
        self._read()

        # 1. protoheader
        if self._jsonheader_len is None:
            self.process_protoheader()

        # 2. jsonheader
        if self._jsonheader_len is not None:
            if self.jsonheader is None:
                self.process_jsonheader()

        # 3. content
        if self.jsonheader:
            if self.request is None:
                self.process_request()

    def write(self):
        # 1. create message
        if self.request:
            if not self.response_created:
                self.create_response()

        # 2. send
        self._write()

    def _write(self):
        """Override to close when the response has been sent."""
        if self._send_buffer:
            log.info(f'sending {repr(self._send_buffer)} to {self.addr}')
            try:
                # should be ready to write
                sent = self.sock.send(self._send_buffer)
            except BlockingIOError:
                # Resource Temporarily unavailable (Errno EWOULDBLOCK)
                pass
            else:
                self._send_buffer = self._send_buffer[sent:]
                # close when the buffer is drained. The response has been sent.
                if sent and not self._send_buffer:
                    self.close()

    def process_inc_json(self, data):
        self.request = data

    def process_inc_binary(self, data):
        self.request = data

    # --- extensions ---

    def process_request(self):
        self.process_incoming_message()
        self._set_selector_events_mask('w')

    def _create_response_json_content(self):
        action = self.request.get('action')
        # list files
        if action == 'list-files':
            content = {'result': self.files.list_files()}
        # remove file
        elif action == 'remove-file':
            pass
        # get file (send file)
        elif action == 'get-file':
            pass
        else:
            content = {'result': f'Error: invalid action "{action}".'}
        content_encoding = 'utf-8'
        response = {
            'content_bytes': json_encode(content, content_encoding),
            'content_type': 'text/json',
            'content_encoding': content_encoding,
        }
        return response

    def _create_response_binary_content(self):
        # send file
        pass

    def create_response(self):
        """Create the response message and add it to the buffer"""
        if self.jsonheader['content-type'] == 'text/json':
            response = self._create_response_json_content()
        else:
            response = self._create_response_binary_content()
        message = self._create_message(**response)
        self.response_created = True
        self._send_buffer += message
