def memo(f):
    cache = {}

    def inner(n):
        assert n >= 0
        if n not in cache:
            cache[n] = n if n <= 1 else inner(n - 1) + inner(n - 2)
        return cache[n]

    return inner

