import typing as t


def input_new_list() -> list:
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def get_a_b(numbers: list, counter: int) -> t.Tuple[int, int]:
    return numbers[counter], numbers[counter + 1]


def is_a_bgr_b(a: int, b: int) -> bool:
    return a > b


def swap_list_a_b(numbers: list, c: int) -> list:
    numbers[c], numbers[c + 1] = numbers[c + 1], numbers[c]
    return numbers


def is_end_list(numbers: list, counter: int) -> bool:
    return len(numbers) == counter + 1


def has_swapped(a: int, b: int) -> bool:
    return is_a_bgr_b(a, b)


numbers = input_new_list()
counter = 0
swap = False
while True:
    a, b = get_a_b(numbers, counter)
    if is_a_bgr_b(a, b):
        swap = True
        numbers = swap_list_a_b(numbers, counter)
    counter += 1
    if is_end_list(numbers, counter):
        if not swap:
            break
        swap = False
        counter = 0

print(numbers)
