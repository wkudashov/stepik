import time
from matplotlib import pyplot as plt


def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


def fib2(n):
    f1, f2 = 0, 1
    for i in range(n):
        f1, f2 = f2, (f1 + f2) % 10
    return f1


def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
        plt.legend()
        plt.grid(True)
    plt.show()


# print(timed(fib_digit, 80000))
compare([fib2], list(range(501)))
