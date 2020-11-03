import sys
import unittest
import selectors
import struct
from unittest.mock import Mock, patch

from shared.base import MessageBase
from shared.utils import json_encode

# disable logger
import logging
logging.getLogger('shared.base').setLevel(50)


def mock_message():
    return MessageBase(
            selector=Mock(),
            sock=Mock(),
            addr=Mock(),
            files=Mock()
        )


class MessageBaseTests(unittest.TestCase):

    #
    # _set_selector_events_mask(self, mode)
    #
    def test__set_selector_events_mask_ok(self):
        message = mock_message()
        cases = (
            ('r', selectors.EVENT_READ),
            ('w', selectors.EVENT_WRITE),
            ('rw', selectors.EVENT_READ | selectors.EVENT_WRITE)
        )
        for check, expected in cases:
            with self.subTest(check=check, expected=expected):
                message._set_selector_events_mask(check)
                message.selector.modify.assert_called_with(message.sock, expected, data=message)

    def test__set_selector_events_mask_fail(self):
        message = mock_message()
        with self.assertRaises(ValueError):
            message._set_selector_events_mask('fail')
        message.selector.modify.assert_not_called()

    #
    # process_events(self, mask)
    #
    def test_process_events(self):
        message = mock_message()
        cases = (
            ('r', selectors.EVENT_READ),
            ('w', selectors.EVENT_WRITE),
            ('rw', selectors.EVENT_READ | selectors.EVENT_WRITE),
        )
        for mode, mask in cases:
            with self.subTest(mode=mode, mask=mask):
                message.read = Mock()
                message.write = Mock()
                message.process_events(mask)
                if 'r' in mode:
                    message.read.assert_called_once()
                else:
                    message.read.assert_not_called()
                if 'w' in mode:
                    message.write.assert_called_once()
                else:
                    message.write.assert_not_called()

    #
    # close(self)
    #
    def test_close_delete_socket_ref(self):
        message = mock_message()
        message.close()
        self.assertIsNone(message.sock)

    @patch('shared.base.log')
    def test_close_selector_log_exception(self, log):
        message = mock_message()
        message.selector.unregister.side_effect = Exception()
        message.close()
        log.exception.assert_called_once()

    @patch('shared.base.log')
    def test_close_sock_log_exception(self, log):
        message = mock_message()
        message.sock.close.side_effect = OSError()
        message.close()
        log.exception.assert_called_once()

    #
    # read(self), write(self)
    #
    def test_generic_not_implemented_fail(self):
        """Does not include `handle_message`"""
        message = mock_message()
        cases = (
            'read',
            'write',
        )
        for method in cases:
            with self.subTest(method=method):
                with self.assertRaises(NotImplementedError):
                    getattr(message, method)()

    #
    # _read(self)
    #
    def test__read_one_ok(self):
        message = mock_message()
        message.sock.recv.return_value = b'123123123123'
        message._read()
        self.assertEqual(message._recv_buffer, b'123123123123')
        # message.sock.recv.assert_called_once()

    def test__read__two_ok(self):
        message = mock_message()
        message.sock.recv.return_value = b'123123123123'
        message._read()
        message._read()
        self.assertEqual(message._recv_buffer, b'123123123123'*2)
        # self.assertEqual(2, len(message.sock.recv.mock_calls))

    def test__read_two_fail_second_empty(self):
        message = mock_message()
        message.sock.recv.return_value = b'123123123123'
        message._read()
        message.sock.recv.return_value = b''
        with self.assertRaises(RuntimeError):
            message._read()

    def test__read_except_empty_fail(self):
        message = mock_message()
        message.sock.recv.return_value = b''
        with self.assertRaises(RuntimeError):
            message._read()

    def test__read_pass_if_blocking(self):
        message = mock_message()
        message.sock.recv.side_effect = BlockingIOError()
        message._recv_buffer = b'123123123123'
        message._read()
        self.assertEqual(message._recv_buffer, b'123123123123')
        # message.sock.recv.assert_called_once()

    #
    # _write(self)
    #
    def test__write_ok(self):
        to_send = b'123123123123123123123123'
        cases = (
            # send buffer, data
            (len(to_send), to_send),
            (len(to_send), to_send*2),
        )
        for buffsize, data in cases:
            with self.subTest(buffsize=buffsize, data=data):
                message = mock_message()
                message._send_buffer = data
                message.sock.send.return_value = buffsize
                expected = len(data) - buffsize

                message._write()
                self.assertEqual(len(message._send_buffer), expected)

    def test__write_pass_if_blocking(self):
        message = mock_message()
        message.sock.send.side_effect = BlockingIOError()
        message._send_buffer = b'123123123123'
        message._write()
        self.assertEqual(message._send_buffer, b'123123123123')

    @patch('shared.base.log')
    def test__write_do_nothing_if_buffer_empty(self, log):
        """check if log.trace was called, this is the first thing that happens when _write is called."""
        message = mock_message()
        message._write()
        log.trace.assert_not_called()

    #
    # _create_message(self, *, content_bytes, content_type, content_encoding, content_name=None)
    #
    def test__create_message_ok(self):
        # yikes
        args = {
            'content_bytes': b'data',
            'content_type': 'text/json',
            'content_encoding': 'utf-8',
            'content_name': None
        }
        jsonheader = {
            'byteorder': sys.byteorder,
            'content-type': args['content_type'],
            'content-encoding': args['content_encoding'],
            'content-length': len(args['content_bytes']),
            'content-name': args['content_name']
        }

        jsonheader_bytes = json_encode(jsonheader, 'utf-8')
        json_len = len(jsonheader_bytes)

        message = mock_message()
        message_bytes = message._create_message(**args)

        proto = message_bytes[:2]
        message_bytes = message_bytes[2:]
        self.assertEqual(proto, struct.pack('>H', json_len))

        json = message_bytes[:json_len]
        message_bytes = message_bytes[json_len:]
        self.assertEqual(json, jsonheader_bytes)

        content = message_bytes
        self.assertEqual(content, args['content_bytes'])

    #
    # process_protoheader(self)
    #
    def test_process_protoheader_only_ok(self):
        message = mock_message()
        sample_content_len = 17
        message._recv_buffer = struct.pack('>H', sample_content_len)
        message.process_protoheader()
        self.assertEqual(message._jsonheader_len, sample_content_len)
        self.assertEqual(len(message._recv_buffer), 0)

    def test_process_protoheader_not_more(self):
        message = mock_message()
        sample_content_len = 17
        padding = bytes(10)
        message._recv_buffer = struct.pack('>H', sample_content_len) + padding
        message.process_protoheader()
        self.assertEqual(message._jsonheader_len, sample_content_len)
        self.assertEqual(len(message._recv_buffer), len(padding))

    def test_process_protoheader_skip_not_enough_data(self):
        message = mock_message()
        message._recv_buffer = bytes(1)
        message.process_protoheader()
        self.assertEqual(message._recv_buffer, bytes(1))
        self.assertIs(message._jsonheader_len, None)

    #
    # process_jsonheader(self)
    #
    def test_process_jsonheader_not_more(self):
        message = mock_message()
        jsonheader = {
            'byteorder': 's',
            'content-type': 's',
            'content-encoding': 's',
            'content-length': 1,
            'content-name': 's',
        }
        jsonheader_bytes = json_encode(jsonheader, 'utf-8')
        message._recv_buffer = jsonheader_bytes + bytes(10)
        message._jsonheader_len = len(jsonheader_bytes)
        message.process_jsonheader()
        self.assertEqual(len(message._recv_buffer), len(bytes(10)))
        self.assertEqual(jsonheader, message.jsonheader)

    def test_process_jsonheader_exception_missing_required_header(self):
        template_jsonheader = {
            'byteorder': 's',
            'content-type': 's',
            'content-encoding': 's',
            'content-length': 1,
            # 'content-name' is not required
        }
        for required_header in template_jsonheader:
            message = mock_message()
            jsonheader = template_jsonheader.copy()
            del jsonheader[required_header]
            jsonheader_bytes = json_encode(jsonheader, 'utf-8')
            message._jsonheader_len = len(jsonheader_bytes)
            message._recv_buffer = jsonheader_bytes
            with self.subTest(message=message):
                with self.assertRaises(ValueError):
                    message.process_jsonheader()

    def test_process_jsonheader_skip_not_enough_data(self):
        message = mock_message()
        message._jsonheader_len = 10
        message._recv_buffer = bytes(5)
        message.process_jsonheader()
        self.assertEqual(message._recv_buffer, bytes(5))
        self.assertIs(message.jsonheader, None)

    #
    # process_message(self)
    #
    def test_process_message_skip_not_enough_data(self):
        message = mock_message()
        message.handle_message = Mock()
        message.jsonheader = {'content-length': 10}
        message._recv_buffer = bytes(9)
        message.process_message()
        self.assertEqual(message._recv_buffer, bytes(9))
        message.handle_message.assert_not_called()

    @patch('shared.base.json_decode')
    def test_process_message_read_content_length_no_json_decode(self, json):
        message = mock_message()
        message.handle_message = Mock()
        message.jsonheader = {'content-length': 10, 'content-type': 'binary/custom'}
        message._recv_buffer = bytes(20)
        message.process_message()
        self.assertEqual(message._recv_buffer, bytes(10))
        message.handle_message.assert_called_once_with(bytes(10))
        json.assert_not_called()

    @patch('shared.base.json_decode')
    def test_process_message_read_content_length_json_decode_ok(self, json):
        message = mock_message()
        message.handle_message = Mock()
        message.jsonheader = {'content-length': 10,
                              'content-type': 'text/json',
                              'content-encoding': 'utf-8'}
        message._recv_buffer = bytes(20)
        json.return_value = bytes(10)
        message.process_message()
        self.assertEqual(message._recv_buffer, bytes(10))
        message.handle_message.assert_called_once_with(bytes(10))
        json.assert_called_once_with(bytes(10), 'utf-8')

    #
    # handle_message(self, data)
    #
    def test_handle_message_not_implemented_fail(self):
        message = mock_message()
        with self.assertRaises(NotImplementedError):
            message.handle_message(None)
