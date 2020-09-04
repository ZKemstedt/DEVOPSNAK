def uppg1():
    """# Uppgift 1
    # Skriv ett program som hälsar användaren 10 gånger
    """

    for i in range(10):
        print("Hello User")


def uppg2():
    """# Uppgift 2
    # Skriv ett program (med for-loop) som skriver ut följande:
    #   1
    #   22
    #   333
    #   4444
    #   55555
    #   666666
    #   7777777
    #   88888888
    #   999999999
    """

    print('\n'.join(
        [''.join([f'{i}' for j in range(i)]) for i in range(1, 10)]
        ))


def uppg3():
    """ # Uppgift 3
    # Skriv ett program som låter användaren gissa vilket tal du tänker på
    # tills användaren gissar rätt.
    # Talet har du hårdkodat in i programmet och gissningen från användaren
    # hämtas in via input gång på gång tills dess att gissning == input.
    """

    number = 42  # obviously
    while True:
        try:
            guess = int(input("Enter your guess\n>> "))
        except Exception:
            break
        if guess < number:
            print('Incorrect! Your guess is too low...')
        elif guess > number:
            print('Incorrect! Your guess is too high...')
        elif guess == number:
            print('You guessed correctly! Well done.')
            break


def uppg4():
    """# Uppgift 4
    # Skriv ett program som loopar över en lista innehållandes olika tal.
    # Om programmet stöter på ett ojämnt tal skrivs orden "Not allowed!"
    # ut och loopen avbryts.
    """

    for i in [0, 2, 4, 6, 8, 10, 11, 12, 13, 14, 15]:
        if i % 2 == 1:
            print('Not allowed!')
            break
        else:
            print(f'{i}\t:Ok!')


def uppg5():
    """# Uppgift 5
    # Genom att använda en for-loop, skriv ett program som
    # för varje tal i second_list, hämtar talet och dess position
    # i first_list och skriver resultatet som en lista av tupler.
    # Exempel:
    # first_list = [3, 7, 9, 2, 6]
    # second_list = [2, 3, 6, 7, 9]
    # Output: [(2, 3), (3, 0), (6, 4), (7, 1), (9, 2)]
    """

    first_list = [3, 7, 9, 2, 6]
    second_list = [2, 3, 6, 7, 9]

    tuple_list = []
    for i in second_list:
        tuple_list.append((i, first_list.index(i)))
    print(tuple_list)

    # alternativt
    # print([(i, first_list.index(i)) for i in second_list])


def uppg6():
    """# Uppgift 6
    # Upprepa uppgiften ovan, men använd denna gång list comprehension
    # för att lösa problemet.
    """

    first_list = [3, 7, 9, 2, 6]
    second_list = [2, 3, 6, 7, 9]

    print(*[(1, first_list.index(i)) for i in second_list], sep='\n')


def uppg7():
    """# Uppgift 7
    # Du har följande lista på frukter:
    # fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
    # Skriv ett program som frågar användaren efter hur många platser för
    # frukt hen har i sin korg, och sedan fyller du denna korg (en lista)
    # med frukter genom att loopa igenom frukt-listan tills dess att
    # korg-listan är full.
    # Output-exempel:
    # My_basket = ['apple', 'orange', 'pear', 'banana', 'grapes', 'apple',
    #              'orange', 'pear']
    """

    fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']

    try:
        slots = int(input('How many fruit slots in your bag?\n>> '))
    except TypeError:
        pass

    if slots:
        print('I put some fruits in your bag:\n' +
              ', '.join([fruits[slot % len(fruits)] for slot in range(slots)]))


def uppg8():
    """# Uppgift 8
    # Skriv ett program som använder sig av nästade while-loopar för att skriva
    # ut alla primtal som är mindre än 100.
    # Vägledning: Primtal är ett tal som är större än 1 och som inte går att
    # dela jämt med något tal annat än sig själv och 1. se wikipedia för hur
    # man kan beräkna vad som är ett primtal
    # Exempel på primtal är 2, 3, 5, 7, 11, 13, 17 och 19
    # 4, 6, 8, 9, 10, 12, 14, 15, 18 och 20 är inte primtal
    # (eftersom t.ex 20/5=4, 14/7=2 osv)
    """

    number = 2
    while number < 100:
        div = 2
        prime = True
        while div < number:
            if number % div == 0:
                prime = False
                break
            div += 1
        if prime:
            print(f'{number}', sep=', ')
        number += 1


def uppg8v2():
    """# Uppgift 8 v2
    for/for
    """

    for number in range(2, 101):
        prime = True
        for div in range(2, number):
            if number % div == 0:
                prime = False
                break
        if prime:
            print(f'{number}', sep=', ')


def uppg8v3():
    """ # Uppgift 8 v3
    # list comprehension/list comprehension
    # Radbruten för ökad läsbarhet
    """

    print(', '.join(
        [str(number) for number in range(2, 101) if not any(
            [number % div == 0 for div in range(2, number)]
            )]
        ))


if __name__ == "__main__":
    uppgift_spacer = '\n====================================================\n'
    run_uppg = {
        '1': False, '2': False,
        '3': False, '4': False,
        '5': True, '6': False,
        '7': False, '8': False,
        '8v2': False, '8v3': False
    }

    for i in run_uppg:
        if run_uppg[i]:
            print(uppgift_spacer)
            uppg = locals()[f'uppg{i}']
            print(uppg.__doc__)
            uppg()

    print(uppgift_spacer)
    print('\t\t Run completed.')
    print(uppgift_spacer)
