from .validation import validate_args


def parse(arg: str) -> dict:
    'Convert a series of zero or more numbers to an argument tuple'
    return dict(map(validate_args, arg.split()))


def dict_to_str(options: dict) -> str:
    return ", ".join(map(lambda x: f'{x[0]}={x[1]}', options.items()))
