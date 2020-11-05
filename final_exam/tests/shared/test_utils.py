import unittest

from shared.utils import (
    json_encode,
    json_decode,
    create_json_content,
    create_json_request,
    create_json_response,
    create_binary_content,
    create_binary_request,
    create_binary_response,
    check_timediff
)

# disable logger
import logging
logging.getLogger('shared.utils').setLevel(50)

# sample data
json_content = {'sample': 'content'}
json_encoding = 'utf-8'
binary_data = bytes(10)
binary_name = 'sample name'


def template_json(content=json_content, encoding=json_encoding):
    """This is how the json content should look."""
    return {
        'content_type': 'text/json',
        'content_encoding': encoding,
        'content_bytes': json_encode(content, encoding)
    }


def template_binary(data=binary_data):
    """This is how the binary content should look."""
    return {
        'content_type': 'binary/custom',
        'content_encoding': 'binary',
        'content_bytes': data
    }


def template_binary_with_name(data=binary_data, name=binary_name):
    """Binary content can optionally contain an extra item ('content_name': name)"""
    template = template_binary(data)
    template.update({'content_name': name})
    return template


class UtilsTests(unittest.TestCase):

    def test_json_encode_decode_ok(self):
        data = json_encode(json_content, json_encoding)
        result = json_decode(data, json_encoding)
        self.assertEqual(json_content, result)

    def test_json_encode_decode_data_is_bytes(self):
        data = json_encode(json_content, json_encoding)
        self.assertIsInstance(data, bytes)

    def test_create_json_content_ok(self):
        result = create_json_content(json_content)
        json = template_json()
        self.assertEqual(json, result)

    def test_json_request_ok(self):
        action = 'sample'
        value = 'sample'
        json = template_json(content={'action': action, 'value': value})
        result = create_json_request(action, value)
        self.assertEqual(json, result)

    def test_json_response_ok(self):
        result = 'sample'
        data = 'sample'
        json = template_json(content={'result': result, 'data': data})
        result = create_json_response(result, data)
        self.assertEqual(json, result)

    def test_create_binary_and_aliases_ok(self):
        cases = (
            (template_binary(), create_binary_content(binary_data)),
            (template_binary(), create_binary_request(binary_data)),
            (template_binary(), create_binary_response(binary_data)),
            (template_binary_with_name(), create_binary_content(binary_data, binary_name)),
            (template_binary_with_name(), create_binary_request(binary_data, binary_name)),
            (template_binary_with_name(), create_binary_response(binary_data, binary_name))
        )
        for first, second in cases:
            with self.subTest(first=first, second=second):
                self.assertEqual(first, second)

    def test_check_timediff_ok(self):
        """
        Should return true if t1 is within 10 of t2
        Both ints and floats should work.
        """
        cases = (
            (0, 0, True),
            (10, 0, True),
            (-5, 5, True),
            (5, -5, True),
            (0, 10, True),

            (10, -10, False),
            (0, 11, False),
            (0, -11, False),
            (-1, -20, False),
            (1, 20, False)
        )
        for t1, t2, expect in cases:
            with self.subTest(t1=t1, t2=t2, exp=expect):
                self.assertEqual(check_timediff(t1, t2), expect)
