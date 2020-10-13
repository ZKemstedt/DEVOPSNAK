import unittest
from unittest.mock import patch

from lesson_3.deploy_cli import DeployTool


class CmdTests(unittest.TestCase):

    def test_do_bye_returns_true(self):
        self.assertEqual(DeployTool().do_bye(""), True)

    def test_do_restart_return_false_on_validationerror(self):
        self.assertEqual(DeployTool().do_restart('scv=value'), False)

    def test_do_restart_return_false_on_typeerror(self):
        with patch('lesson_3.deploy_cli.restart') as m, patch('lesson_3.deploy_cli.parse') as n:
            m.side_effect = TypeError
            n.return_value = dict([('service', 5)])
            self.assertEqual(DeployTool().do_restart(''), False)

    def test_do_restart_return_false_on_fail(self):
        with patch('lesson_3.deploy_cli.restart') as m:
            m.return_value = 255
            self.assertEqual(DeployTool().do_restart(''), 255)

    def test_do_restart_return_false_on_success(self):
        with patch('lesson_3.deploy_cli.restart') as m:
            m.return_value = False
            self.assertEqual(DeployTool().do_restart(''), False)

    def test_do_deploy_return_false_on_validationerror(self):
        self.assertEqual(DeployTool().do_deploy('scv=value'), False)

    def test_do_deploy_return_false_on_typeerror(self):
        with patch('lesson_3.deploy_cli.deploy') as m, patch('lesson_3.deploy_cli.parse') as n:
            m.side_effect = TypeError
            n.return_value = dict([('service', 5)])
            self.assertEqual(DeployTool().do_deploy(''), False)

    def test_do_deploy_return_false_on_fail(self):
        with patch('lesson_3.deploy_cli.deploy') as m:
            m.return_value = 255
            self.assertEqual(DeployTool().do_deploy(''), 255)

    def test_do_deploy_return_false_on_success(self):
        with patch('lesson_3.deploy_cli.deploy') as m:
            m.return_value = False
            self.assertEqual(DeployTool().do_deploy(''), False)

    def test_postcmd_hook_exit_with_int(self):
        with patch('lesson_3.sys.exit') as m:
            m.side_effect = Exception
            with self.assertRaises(Exception):
                DeployTool().postcmd(255, '')

    def test_postcmd_hook_return_if_not_int(self):
        self.assertEqual(DeployTool().postcmd('yes', ''), 'yes')


if __name__ == '__main__':
    unittest.main()
