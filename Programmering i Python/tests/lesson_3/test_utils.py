import unittest
from lesson_3.cli_tool import utils


class UtilsTests(unittest.TestCase):

    def test_parse_args(self):
        result = utils.parse("conf=prod service=backend")
        self.assertIsInstance(result, dict)
        self.assertEqual(result, {"conf": "prod", "service": "backend"})

    def test_dict_to_str(self):
        self.assertEqual(utils.dict_to_str({"conf": "prod", "service": "backend"}), "conf=prod, service=backend")


if __name__ == '__main__':
    unittest.main()
