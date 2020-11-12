import unittest
from lesson_3.cli_tool import validation


class ValidationTests(unittest.TestCase):

    # -- validate_args --
    def test_validate_args(self):
        valid_keys = ['region',  'service', 'conf', 'cluster', 'timeout']
        for key in valid_keys:
            self.assertEqual(validation.validate_args(f'{key}=test'), [key, 'test'])

    def test_validate_args_fail_invalid_key(self):
        with self.assertRaises(validation.ValidationError):
            validation.validate_args('legion=test')

    def test_validate_args_fail_invalid_format(self):
        with self.assertRaises(validation.ValidationError):
            validation.validate_args('region')

    # -- deploy_options --
    def test_validate_deploy_options_fail_not_dict(self):
        with self.assertRaises(AttributeError):
            validation.validate_deploy_options(5)

    def test_validate_deploy_options_fail_option_not_str(self):
        with self.assertRaises(TypeError):
            validation.validate_deploy_options({'conf': 5})

    # -- validate_conf --
    def test_validate_conf_fail_not_string(self):
        with self.assertRaises(TypeError):
            validation.validate_conf(5)

    def test_validate_conf_is_string(self):
        self.assertEqual(validation.validate_conf('key', 'value'), None)


if __name__ == '__main__':
    unittest.main()
