import itertools


def primes():
    number = 0
    while True:
        if list(map(lambda _: number % _ == 0, range(1, number + 1))).count(True) == 2:
            yield number
        number += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
