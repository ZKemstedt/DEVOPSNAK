import logging

from shared.base import MessageBase
from shared.utils import json_encode

log = logging.getLogger(__name__)


class Message(MessageBase):

    # --- overrides ---

    def __init__(self, selector, sock, addr, request):
        super().__init__(selector, sock, addr)
        self.request = request
        self._request_queued = False
        self.response = None

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
                self.process_response()

    def write(self):
        # 1. queue
        if not self._request_queued:
            self.queue_request()

        # 2. send
        self._write()

        # 3. change send -> receive
        if self._request_queued and not self._send_buffer:
            self._set_selector_events_mask('r')

    def process_inc_json(self, data):
        self.response = data
        # TODO
        log.info(f'result: {self.response.get("result")}')

    def process_inc_binary(self, data):
        self.response = data
        # TODO
        log.info('received binary reponse (done)')

    # --- extensions ---

    def process_response(self):
        self.process_incoming_message()
        self.close()

    def queue_request(self):
        """
        Create message and queue it.
        If the content-type is json, encode it.
        """
        _content = self.request['content']
        _type = self.request['type']
        _encoding = self.request['encoding']
        if _type == 'text/json':
            _content = json_encode(_content, _encoding)

        message = self._create_message(
            content_bytes=_content,
            content_type=_type,
            content_encoding=_encoding)
        self._send_buffer += message
        self._request_queued = True
