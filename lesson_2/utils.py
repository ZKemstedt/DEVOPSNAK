from functools import reduce


def multiply(*factor):
    return reduce(lambda x, y: x*y, factor)


def add(*term):
    return sum(term)


def sum_inc_five(*factor):
    return add((*factor), 5)


def decide_branch(decide):
    if(decide):
        return decide
    else:
        return decide
