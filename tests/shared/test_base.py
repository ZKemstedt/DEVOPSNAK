import logging
import unittest
import selectors
from unittest.mock import Mock, patch

from shared.base import MessageBase

# disable logger
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
    def test__create_message(self):
        pass

    #
    # process_protoheader(self)
    #
    def test_process_protoheader(self):
        pass

    #
    # process_jsonheader(self)
    #
    def test_process_jsonheader(self):
        pass

    #
    # process_incoming_message(self)
    #
    def test_process_incoming_message(self):
        pass

    #
    # handle_message(self, data)
    #
    def test_handle_message_not_implemented_fail(self):
        message = mock_message()
        with self.assertRaises(NotImplementedError):
            message.handle_message(None)
