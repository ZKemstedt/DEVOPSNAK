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

    def test_a_text(self):
        type(self.a_thread).a_text = PropertyMock(side_effect=["b", "c", "d", "e"])
        self.a_thread.print_text()
        self.a_thread.print_text()
        self.a_thread.print_text()
        self.a_thread.print_text()

    def tearDown(self):
        type(self.a_thread).running = None
        type(self.a_thread).a_text = None


if __name__ == "__main__":
    unittest.main()
