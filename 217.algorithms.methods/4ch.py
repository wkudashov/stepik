def liner(lines):
    lines.sort(key=lambda x: x[1])
    result = [lines[0][1]]
    for line in lines:
        if line[0] > result[-1]:
            result.append(line[1])
    return result


def main():
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    output = liner(arr)
    print(len(output))
    print(*output, sep=' ')


if __name__ == "__main__":
    main()
