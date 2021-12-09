def pisano(n, m):
    pis = [0, 1]
    if n == 1:
        return pis
    f1, f2 = 0, 1
    for i in range(m*6):
        f1, f2 = f2, (f1 + f2) % m
        pis.append(f2)
        if pis[-2] == 0 and pis[-1] == 1:
            return pis[:-2]


def main():
    # n, m = map(int, input().split())
    n, m = 3232234324241, 6235344
    p = pisano(n, m)
    print(p)
    fib = n % len(p)
    print(fib)


if __name__ == "__main__":
    main()
