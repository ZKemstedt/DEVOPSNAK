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
