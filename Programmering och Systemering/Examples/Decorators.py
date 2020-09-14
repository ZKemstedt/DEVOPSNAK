# Enforce function argument and return types.
#       https://www.python.org/dev/peps/pep-0318/

# Zephyro version
import inspect
from functools import wraps


def print_type_annotations(placeholder_arg=None):
    """placeholder docstring"""
    # this step is for future development
    def decorator(f):
        sig = inspect.signature(f)
        print(f'parameters of function {f.__qualname__}')
        for name, param in sig.parameters.items():
            print(f'Param: {name}: {param.annotation}')
        print(f'return annotation: {sig.return_annotation}')

        return f
    return decorator


class ConversionException(Exception):
    pass


def int_converter(i) -> int:
    """convert a given value to int, raise ConversionException if error"""
    try:
        return int(i)
    except ValueError:
        raise ConversionException


def get_converter():
    pass


def ensure_arg_types(fail_ok: bool = True):
    """"""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwds):
            print('calling decorated function')
            for param in inspect.signature(f).parameters.values():
                default = param.default
                _type = param.annotation
                print(f'default: {default}, type: {_type}')
            return f(*args, **kwds)
        return wrapper
    return decorator
# for name, param.bind()
# bound_args.apply_defaults()

# pass


# @print_type_annotations()
@ensure_arg_types()
def add(a: int = 0, b: int = 0) -> int:
    """add two arguments and return the sum"""
    return a + b


if __name__ == "__main__":
    print(add(1, 2))
