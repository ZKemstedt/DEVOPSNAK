from random import randint


def rng(_max: int = 100, amount: int = 20) -> list:
    numbers = []
    for _ in range(amount):
        numbers.append(randint(0, _max))
    return numbers


def get_user_number() -> str:
    while True:
        try:
            return int(input("Ange ett tal: "))
        except KeyboardInterrupt:
            quit()
        except ValueError:
            pass


def odd_numbers(number_list: list) -> list:
    return [x for x in number_list if x % 2 != 0]


specials = []
limit = get_user_number()
for number in odd_numbers(rng(_max=100, amount=20)):
    if number < limit:
        specials.append(number)

print(specials)
