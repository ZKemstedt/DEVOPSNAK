primes = [2]

for number in range(3, 1000):
    prime = True
    for prime in primes:
        if prime * prime >= number:
            break
        if number % prime == 0:
            break


print(primes)
