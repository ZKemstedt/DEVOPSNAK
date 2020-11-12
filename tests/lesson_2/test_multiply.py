import unittest
from lesson_2 import utils


class HappyPathTestCase(unittest.TestCase):

    def test_ones(self):
        self.assertEqual(utils.multiply(1, 1), 1)

    def test_negative_ones(self):
        self.assertEqual(utils.multiply(-1, -1), 1)

    def test_float_ones(self):
        self.assertEqual(utils.multiply(1.0, 1.0), 1.0)

    def test_one_multiply_by_2(self):
        self.assertEqual(utils.multiply(1, 2), 2)

    def test_multiply_same(self):
        self.assertEqual(utils.multiply(2, 2), 4)

    def test_multiply_range(self):
        self.assertEqual(utils.multiply(1, 2, 3, 4), 24)


class NegativeTestCase(unittest.TestCase):

    def test_to_multiply_empty(self):
        with self.assertRaises(TypeError):
            utils.multiply()

    def test_to_multiply_two_string(self):
        with self.assertRaises(TypeError):
            utils.multiply("2", "2")

    def test_to_multiply_string_and_int(self):
        with self.assertRaises(TypeError):
            utils.multiply("2", 2)

    def test_to_multiply_tuple(self):
        with self.assertRaises(TypeError):
            utils.multiply((1, 2), (3, 4))


if __name__ == '__main__':
    unittest.main()
