import random
import time
from matplotlib import pyplot as plt


def timed(f, n_iter):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        test_gcd(f, n_iter)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
        plt.legend()
        plt.grid(True)
    plt.show()


def test_gcd(gcd, n_iter):
    for i in range(n_iter):
        c = random.randint(1, 1024)
        a = c * random.randint(0, 128)
        b = c * random.randint(1, 128)
        # assert a + b != 0
        assert gcd(a, a) == gcd(a, 0) == a
        assert gcd(b, b) == gcd(b, 0) == b
        assert gcd(a, 1) == gcd(b, 1) == 1
        d = gcd(a, b)
        assert a % d == b % d == 0
    # print(f'function {gcd.__name__} is OK')


def gcd1(a, b):
    assert a >= 0 and b >= 0
    for d in reversed(range(1, max(a, b) + 1)):
        if a % d == b % d == 0:
            return d
    return 0


def gcd2(a, b):
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return a + b


def gcd3(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return a + b
    elif a >= b:
        return gcd3(a % b, b)
    else:
        return gcd3(a, b % a)


def gcd4(a, b):
    a, b = sorted([a, b])
    while a:
        a, b = b % a, a
    return b


def gcd5(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return a + b
    return gcd3(b % a, a)


def main():
    # n, m = map(int, input().split())
    # print(gcd3(n, m))
    compare([gcd2, gcd3, gcd4, gcd5], list(range(50)))


if __name__ == "__main__":
    main()
