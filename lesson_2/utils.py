from functools import reduce


def multiply(*factor):
    for f in factor:
        if not isinstance(f, (int, float)):
            raise TypeError("Only int is allowed as type")
    return reduce(lambda x, y: x*y, factor)


def add(*term):
    return sum(term)


def decide_branch(decide):
    if(decide):
        return decide
    else:
        return decide
