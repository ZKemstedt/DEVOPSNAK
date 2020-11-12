import unittest
from unittest.mock import patch

from lesson_3.cli_tool import api
from lesson_3.cli_tool.validation import DeployException


class APITests(unittest.TestCase):

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

    def test_restart(self):
        with patch('lesson_3.cli_tool.api.fake_restart') as m:
            m.return_value = None
            result = api.restart()
            self.assertEqual(result, False)

    def test_restart_failure(self):
        with patch('lesson_3.cli_tool.api.fake_restart') as m:
            m.side_effect = Exception()
            result = api.restart()
            self.assertEqual(result, 255)


if __name__ == '__main__':
    unittest.main()
