import functools

VALID_KEYS = ["region", "service", "conf"]


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


def validate_conf(conf):
    if not isinstance(conf, str):
        raise TypeError("conf should be of type str")


def validate_deploy_options(options):
    validate_conf(options.get("conf"))


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
