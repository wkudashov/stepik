def max_cost(w, arr):
    stuff = [0, 0]
    for item in sorted(arr, key=lambda x: x[0] / x[1], reverse=True):
        if stuff[1] < w and item[1] <= w - stuff[1]:
            stuff[0] += item[0]
            stuff[1] += item[1]
        elif stuff[1] < w and item[1] > w - stuff[1]:
            stuff[0] += item[0] * (w - stuff[1]) / item[1]
            stuff[1] = w
    return f'{stuff[0]:.3f}'


def main():
    n, capacity = map(int, input().split())
    items = [list(map(int, input().split())) for i in range(n)]
    print(max_cost(capacity, items))


if __name__ == "__main__":
    main()