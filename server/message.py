import logging

from shared.base import MessageBase
from shared.utils import create_response

log = logging.getLogger(__name__)


class Message(MessageBase):

    # --- overrides ---

    def __init__(self, selector, sock, addr, filepath):
        super().__init__(selector, sock, addr, filepath)
        self.request = None
        self.response_created = False

    def read(self):
        self._read()

        # 1  protoheader
        if self._jsonheader_len is None:
            self.process_protoheader()

        # 2. jsonheader
        if self._jsonheader_len is not None:
            if self.jsonheader is None:
                self.process_jsonheader()

        # 3. content
        if self.jsonheader:
            if self.request is None:
                self.process_incoming_message()

        # 4. done, set to write
        if self.request:
            self._set_selector_events_mask('w')

    def write(self):
        # 1. create message
        if self.request:
            if not self.response_created:
                self.build_response()

        # 2. send
        self._write()

        # 3. close when done
        if not self._send_buffer:
            self.close()

    def handle_message(self, data):
        self.request = data

    # --- extensions ---

    def build_response(self):
        """Create the response message and add it to the buffer"""
        action = self.request.get('action')
        value = self.request.get('value')

        result = 'success'
        data = None

        if action == 'list-files':
            data = self.files.list_files()

        elif action == 'get-file':
            data = self.files.get_file(value)
            if data is None:
                result = 'error'
                data = f'file named {value} does not exist.'
        else:
            result = 'error'
            data = 'invalid request'

        response = create_response(result, data)
        message = self._create_message(**response)
        self.response_created = True
        self._send_buffer += message
