import unittest
from unittest.mock import MagicMock
from lesson_13.socket_to_test import send_message


class TestHappySock(unittest.TestCase):

    def test_send_msg_as_bytes(self):
        my_mock = MagicMock()
        send_message(my_mock, "hello world")
        my_mock.send.assert_called_once_with(b"hello world")


if __name__ == "__main__":
    unittest.main()
