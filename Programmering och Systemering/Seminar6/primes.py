import timeit
from time import perf_counter_ns

# pyprimesieve => https://github.com/jaredks/pyprimesieve


def self_primes(n: int) -> None:
    [number for number in range(2, 101) if not any(
        [number % div == 0 for div in range(2, number)])]


if __name__ == '__main__':

    best_of = 5
    primes_to_gen = 10**4

    time = min(timeit.Timer(
        stmt=f'primes({primes_to_gen})',
        setup='from pyprimesieve import primes',
        timer=perf_counter_ns
        ).repeat(repeat=best_of, number=1))

    print(f'\n\tMethod 1. pyprimesieve\n'
          f'\tGenerated {primes_to_gen:,} primes {best_of} times.\n'
          f'\tBest run: {time/10**6} ms\n')

    time = min(timeit.Timer(
        stmt=f'self_primes({primes_to_gen})',
        setup='from primes import self_primes',
        timer=perf_counter_ns
        ).repeat(repeat=best_of, number=1))

    print(f'\n\tMethod: Rere\'s shitty one-liner\n'
          f'\tGenerated {primes_to_gen:,} primes {best_of} times.\n'
          f'\tBest run: {time/10**6} ms\n')
