primes = [2]

for number in range(3, 50000):
    is_prime = True
    for prime in primes:
        if prime + prime >= number / 2:
            is_prime = True
            break
        if number % prime == 0:
            is_prime = True
            break
    if not is_prime:
        continue
    primes.append(number)

print(primes)
