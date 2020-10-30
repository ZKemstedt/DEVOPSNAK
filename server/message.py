import logging

from shared.base import MessageBase
from shared.utils import create_json_response, create_binary_response

log = logging.getLogger(__name__)


class Message(MessageBase):

    # --- overrides ---

    def __init__(self, selector, sock, addr, files):
        super().__init__(selector, sock, addr, files)
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
        file = None

        if self.jsonheader['content-type'] == 'binary/custom':
            name = self.jsonheader.get('content-name', None)
            if name:
                self.files.write_file(name, self.request)
                result = 'success'
            else:
                result = 'error'
            response = create_json_response(result, None)
        else:
            action = self.request.get('action')
            value = self.request.get('value')
            log.info(f'request: {action} ({value}) from {self.addr}')

            if action == 'get-file':
                file = self.files.get_file(value)
                if file is None:
                    result = 'error'
                    data = f'file named {value} does not exist.'
                    response = create_json_response(result, data)
                else:
                    result = 'success'
                    data = {'file-length': f'{len(file)}'}
                    response = create_binary_response(file)
            else:

                if action == 'list-files':
                    result = 'success'
                    data = self.files.list_files()

                elif action == 'remove-file':
                    data = self.files.remove_file(value)
                    result = 'succcess' if data is None else 'error'

                elif action == 'request-register':
                    result = 'success'
                    data = self.files.register

                else:
                    result = 'error'
                    data = 'invalid request'

                response = create_json_response(result, data)
        log.info(f'result built: {response}')
        message = self._create_message(**response)
        self._send_buffer += message
        self.response_created = True
