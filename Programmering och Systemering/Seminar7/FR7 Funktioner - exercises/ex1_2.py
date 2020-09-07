def repeat_printer(number: str) -> None:
    """prints the input `number`, `number` amount of times"""
    number = int(number)
    print(f'svar: {number}'*number)


number = input("Ange ett tal: ")

if number <= 5:
    for i in range(1, number+1):
        repeat_printer(number)
else:
    repeat_printer(number)
