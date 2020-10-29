import io
import json
import logging

log = logging.getLogger(__name__)


def json_encode(obj, encoding):
    return json.dumps(obj, ensure_ascii=False).encode(encoding)


def json_decode(json_bytes, encoding):
    with io.TextIOWrapper(io.BytesIO(json_bytes), encoding=encoding, newline='') as tiow:
        obj = json.load(tiow)
    return obj


def create_request(action, value):
    content = {'action': action, 'value': value}
    return {
        'content-type': 'text/json',
        'content-encoding': 'utf-8',
        'content-bytes': json_encode(content, 'utf-8'),
    }


def create_response(result, data):
    content = {'result': result, 'data': data}
    return {
        'content-type': 'text/json',
        'content-encoding': 'utf-8',
        'content-bytes': json_encode(content, 'utf-8'),
    }
