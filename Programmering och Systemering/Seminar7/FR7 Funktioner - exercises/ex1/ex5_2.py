numbers = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50,
           55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
specials = []

while True:
    try:
        value = int(input("Ange ett tal: "))
        break
    except KeyboardInterrupt:
        quit()
    except ValueError:
        pass

for number in numbers:
    if number % 2 != 0 and number < value:
        specials.append(number)

print(specials)
