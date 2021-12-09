def fib_digit(n):
    f1, f2 = 0, 1
    for i in range(n):
        f1, f2 = f2, (f1 + f2) % 10
    return f1


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
