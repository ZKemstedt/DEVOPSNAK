import timeit
import typing as t
import sys
sys.setrecursionlimit(1500)

# numbers = [1, 9, 0, 5, 18, 4, 12, 6, 8, 14, 7, 16, 10, 11, 13, 15, 3, 2, 17]
numbers = [1, 9, 0, 5, 18, 4]


def swap(numbers: t.List[int], i: int) -> t.Tuple[t.List[int], bool]:
    """Set `changes`"""
    numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
    return numbers, True


def swap_if_greater(numbers: t.List[int], changes: bool, i: int
                    ) -> t.Tuple[t.List[int], bool, int]:
    """Incremention of `i`"""
    if numbers[i] < numbers[i - 1]:
        return *swap(numbers, i), i + 1
    return numbers, changes, i + 1


def bubble(numbers: t.List[int], changes: bool = False, i: int = 0
           ) -> t.Tuple[t.List[int], bool]:
    """Initiation of `changes` and `i`"""
    if i >= len(numbers) - 1:
        return numbers, changes
    return bubble(*swap_if_greater(numbers, changes, i + 1))


def bubble_sort(numbers: t.List[int], changes: t.Optional[bool] = True
                ) -> t.List[int]:
    """Redo if `changes`. `changes` defaults to True for init"""
    if changes:
        return bubble_sort(*bubble(numbers))
    return numbers


print(f'Before sort: {numbers}')
sorted_numbers = bubble_sort(numbers)
print(f'Bubble sorted: {sorted_numbers}')

print(timeit.timeit('bubble_sort(numbers)',
                    'from __main__ import bubble_sort, numbers'
                    ))
