import unittest
from lesson_2 import utils


class HappyPathTestCase(unittest.TestCase):

    def test_ones(self):
        self.assertEqual(utils.sum_inc_five(1, 1), 7)

    def test_twos(self):
        self.assertEqual(utils.sum_inc_five(2, 2), 9)

    def test_one_negative(self):
        self.assertEqual(utils.sum_inc_five(2, -2), 5)

    def test_two_negative(self):
        self.assertEqual(utils.sum_inc_five(-2, -2), 1)


class NegativeTestCase(unittest.TestCase):

    def test_to_add_two_string(self):
        with self.assertRaises(TypeError):
            utils.sum_inc_five("2", "2")


if __name__ == '__main__':
    unittest.main()
