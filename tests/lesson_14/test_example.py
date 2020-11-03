import unittest
from lesson_14.example import send_something
from unittest.mock import patch, call


class TestExample(unittest.TestCase):

    @patch('lesson_14.example.sender')
    def test_send_something(self, mock_sender):
        send_something("hej")
        self.assertEqual(mock_sender.call_count, 2)
        expected_calls = [call('person1', 'hej'), call('person2', 'hej')]
        self.assertEqual(mock_sender.mock_calls, expected_calls)


if __name__ == "__main__":
    unittest.main()
