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


def create_json_request(action, value):
    content = {'action': action, 'value': value}
    return create_json(content)


def create_json_response(result, data):
    content = {'result': result, 'data': data}
    return create_json(content)


def create_json(content):
    return {
        'content_type': 'text/json',
        'content_encoding': 'utf-8',
        'content_bytes': json_encode(content, 'utf-8'),
    }


def create_binary_request(data, name=None):
    d = {
        'content_type': 'binary/custom',
        'content_encoding': 'binary',
        'content_bytes': data,
    }
    if name:
        d['content_name'] = name
    return d


def create_binary_response(data, name=None):
    return create_binary_request(data, name)


# def format_time(seconds):
#     value = int(seconds)
#     if value < 99:
#         return f'{value}s'

#     value, unit = rep_div_mod(value, ['m', 'h'], 60, 99)
#     if unit == 'h' and value > 99:
#         value, unit = rep_div_mod(value, ['d'], 24, 60)
#     elif unit == 'd' and value > 30:
#         value, unit = rep_div_mod(value, ['M'], 30, 12)
#     elif unit == 'M' and value > 12:
#         value, units = rep_div_mod(value, ['y'], 12, 99)
#     return f'{value}{unit}'


# def rep_div_mod(lower, units, div, br=99):
#     for unit in units:
#         lower, r = divmod(lower, div)
#         log.debug(f'div: {int(lower)} {unit}')
#         if lower <= br:
#             return lower, unit
#     return lower, unit
