import unittest
from lesson_3.cli_tool import api
from unittest.mock import patch
from lesson_3.cli_tool.validation import DeployException


class UtilsTests(unittest.TestCase):

    def test_deploy(self):
        with patch("lesson_3.cli_tool.api.fake_deploy") as m:
            m.return_value = None
            result = api.deploy()
            self.assertEqual(result, False)

    def test_deploy_failure(self):
        with patch("lesson_3.cli_tool.api.fake_deploy") as m:
            m.side_effect = DeployException()
            result = api.deploy()
            self.assertEqual(result, 255)


if __name__ == '__main__':
    unittest.main()
