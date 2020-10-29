import logging

from shared.base import MessageBase
from shared.utils import create_request

log = logging.getLogger(__name__)


class Message(MessageBase):

    # --- overrides ---

    def __init__(self, selector, sock, addr, filepath, action, value):
        super().__init__(selector, sock, addr, filepath)
        self.request = create_request(action, value)
        self._request_queued = False
        self.response = None
        self.action = action
        self.value = value

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
            if self.response is None:
                self.process_incoming_message()

        # 4. close when done.
        if self.response:
            self.handle_response()
            self.close()

    def write(self):
        # 1. queue
        if not self._request_queued:
            self.queue_request()

        # 2. send
        self._write()

        # 3. change send -> receive
        if self._request_queued and not self._send_buffer:
            self._set_selector_events_mask('r')

    def handle_message(self, data):
        self.response = data

    # --- extensions ---

    def queue_request(self):
        message = self._create_message(**self.request)
        self._send_buffer += message
        self._request_queued = True

    def handle_response(self):
        action = self.action
        value = self.value

        result = self.response.get('result')
        data = self.response.get('data')

        if result == 'error':
            log.info(f'result: {repr(result)}, data: {repr(data)}')
            return

        elif result == 'success':
            if action == 'list-files':
                log.info(data)

            elif action == 'get-file':
                self.files.write_file(value, data)

            # elif action == '':
            #     pass
        else:
            log.debug('code 51')
