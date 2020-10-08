import unittest
from lesson_3.deploy_cli import DeployTool


class CmdTests(unittest.TestCase):

    def test_do_bye_returns_true(self):
        self.assertEqual(DeployTool().do_bye(""), True)


if __name__ == '__main__':
    unittest.main()
