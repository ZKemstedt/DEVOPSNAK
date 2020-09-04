# Bra uppgifter att göra är 5, 8, 10, 11 och 40
# Uppgiftera 2,3, 12, 13 och 44 kan ni hoppa över
# Resterande uppgifter görs i mån av tid.

run_uppg = {
    '1': False,
    '5': False,
    '8': False,
    '10': False,
    '11': False,
    '40': True
}


# 1. Write a Python program to find those numbers which are divisible by 7
# and multiple of 5, between 1500 and 2700 (both included).

if run_uppg['1']:
    print('These values are divisable by 7:')
    print(', '.join(
        [str(x) for x in range(1500, 2701) if x % 5 == x % 7 == 0]))


# 5. Write a Python program that accepts a word from the user and reverse it.

if run_uppg['5']:
    word = input('Input a word to be reversed\n>> ')
    print(word[::-1])


# 8. Write a Python program that prints all the numbers from 0 to 6 except
# 3 and 6. Note : Use 'continue' statement.

if run_uppg['8']:
    forbidden = [3, 6]
    for i in range(7):
        if i in forbidden:
            continue
        print(i)


# 10. Write a Python program which iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number and for the
# multiples of five print "Buzz". For numbers which are multiples of
# both three and five print "FizzBuzz".

if run_uppg['10']:
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


# 11. Write a Python program which takes two digits m (row) and n (column)
# as input and generates a two-dimensional array. The element value in
# the i-th row and j-th column of the array should be i*j.

if run_uppg['11']:
    rows = 3
    columns = 4
    rangex = range(1, rows+1)
    rangey = range(1, columns+1)
    print('\n'.join(
        [('[ '+' '.join([str(x*y) for x in rangex])+' ]')
         for y in rangey]))


# 40. Write a Python program to find the median of three values.

if run_uppg['40']:
    numbers = [15, 26, 29]
    print(f'The median value is: {sorted(numbers)[len(numbers)/2]}')
