import unittest
from unittest.mock import patch
import threading
from lesson_11.threading_example import AThread


def fake_loop(self):
    while self.running:
        pass


class TestAThread(unittest.TestCase):

    def setUp(self):
        self.a_thread = AThread()

    def test_a_thread_is_subclass_thread(self):
        self.assertTrue(issubclass(AThread, threading.Thread))

    def test_a_thread_is_a_thread(self):
        self.assertIsInstance(self.a_thread, threading.Thread)

    def test_a_thread_by_default_not_alive(self):
        self.assertFalse(self.a_thread.is_alive())

    @patch.object(AThread, "loop", fake_loop)
    def test_a_thread_started_is_alive(self):
        self.a_thread.start()
        self.assertTrue(self.a_thread.is_alive())

    def tearDown(self):
        self.a_thread.running = False


if __name__ == '__main__':
    unittest.main()
