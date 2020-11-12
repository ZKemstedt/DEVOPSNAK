from functools import reduce


def multiply(*factor):
    if not all(isinstance(f, int) or isinstance(f, float) for f in factor):
        raise TypeError('arguments must be int')
    return reduce(lambda x, y: x*y, factor)


def add(*term):
    if not all(isinstance(t, int) for t in term):
        raise TypeError('arguments must be int')
    return sum(term)


def sum_inc_five(*term):
    if not all(isinstance(t, int) for t in term):
        raise TypeError('arguments must be int')
    return add((*term), 5)


def decide_branch(decide):
    if(decide):
        return decide
    else:
        return decide
