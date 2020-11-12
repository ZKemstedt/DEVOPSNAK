import unittest
from lesson_5.mora import Mora


class MoraTest(unittest.TestCase):

    def test_brand_string(self):
        watch = Mora("noname", 100)
        self.assertEqual(watch.brand, "noname")


if __name__ == "__main__":
    unittest.main()
