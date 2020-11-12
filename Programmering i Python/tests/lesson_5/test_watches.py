import unittest
from lesson_5.watches import Watches


class WatchTest(unittest.TestCase):

    def test_brand_string(self):
        watch = Watches("rolex")
        self.assertEqual(watch.brand, "rolex")


if __name__ == "__main__":
    unittest.main()
