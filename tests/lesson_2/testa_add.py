import unittest
from lesson_2 import utils


class HappyPathTestCase(unittest.TestCase):

    def test_ones(self):
        self.assertEqual(utils.add(1, 1), 2)

    def test_decide_true(self):
        self.assertEqual(utils.decide_branch(True), True)

    def test_decide_false(self):
        self.assertEqual(utils.decide_branch(False), False)


if __name__ == '__main__':
    unittest.main()
