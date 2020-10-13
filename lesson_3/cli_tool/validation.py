import functools

VALID_KEYS = ["region", "service", "conf", "cluster", "timeout"]


class ValidationError(Exception):
    pass


class DeployException(Exception):
    pass


def validate_args(arg):
    try:
        a, b = arg.split("=")
    except ValueError as e:
        raise ValidationError(f'{e}')
    if a in VALID_KEYS and b:
        return [a, b]
    raise ValidationError(f"Not a valid args: {a}")


def validate_conf(k, v):
    if not isinstance(v, str):
        raise TypeError(f"{k} must be a str.")


def validate_deploy_options(options):
    for k, v in options.items():
        validate_conf(k, v)


def return_on_except(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as ve:
            print(ve)
            return False
        except TypeError as te:
            print(te)
            return False
    return wrapper
