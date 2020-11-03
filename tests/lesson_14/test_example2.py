import unittest
from unittest.mock import MagicMock, PropertyMock
from lesson_14.example_2 import AnThread


class TestExample(unittest.TestCase):

    def setUp(self):
        self.a_thread = AnThread(daemon=True)

    def test_a_thread_stops(self):
        self.a_thread.start()
        self.assertTrue(self.a_thread.is_alive())
        self.a_thread.running = False
        self.a_thread.join()
        self.assertFalse(self.a_thread.is_alive())

    def test_print_something_called(self):
        type(self.a_thread).running = PropertyMock(side_effect=[True, False])
        self.a_thread.print_something = MagicMock()
        self.a_thread.start()

        self.a_thread.print_something.assert_called_once()


if __name__ == "__main__":
    unittest.main()
