import unittest
from unittest.mock import MagicMock
from lesson_5.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_parse_string(self):
        self.assertEqual(self.calculator.parse("1 1"), ["1", "1"])

    def test_calculator_create(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_positive(self):
        self.assertEqual(self.calculator.calc_add(["1", "1"]), 2)

    def test_cli_add_success(self):
        self.calculator.calc_add = MagicMock(return_value=3)
        self.calculator.parse = MagicMock(return_value=["1", "1"])
        self.assertEqual(self.calculator.add("1 1"), False)

    def test_cli_add_failure(self):
        self.calculator.parse = MagicMock(side_effect=TypeError)
        self.assertEqual(self.calculator.add("1 1"), True)


if __name__ == "__main__":
    unittest.main()
