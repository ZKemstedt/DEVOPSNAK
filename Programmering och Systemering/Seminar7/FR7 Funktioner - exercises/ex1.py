number = int(input("Ange ett tal: "))

if number <= 5:
    for i in range(1, number+1):
        print(f'svar: {i}' * i)
else:
    print(f'svar: {i}'*number)
