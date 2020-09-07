import typing as t

operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '%': lambda x, y: x % y
}


def get_user_input() -> t.Tuple[int, int, str]:
    while True:
        try:
            text = input("Ange två tal och ett räknesätt ( + - * / % ): \n>> ")
            x, y, op = text.split(' ')
            x, y = int(x), int(y)
            assert op.strip() in operators
            assert not (y == 0 and op == '/')
            return x, y, op
        except KeyboardInterrupt:
            quit()
        except (ValueError,  AssertionError):
            pass


# Considering the intent of the excersize,
# I feel I should have moved the
# input validation out of the user input function...
# Next time :)
x, y, op = get_user_input()
operation = operators[op]
result = operation(x, y)
print(result)

# One-liner, because I got bored
# Usually these one-liners mean I learn 1 more stupid
# way to do simple things. In this case: eval()
# print(eval('operators[\'{d[2]}\']({d[1]}, {d[0]})'.format(d=get_user_input())))
