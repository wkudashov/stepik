str = input()
in_arr = []
n = 0
m = len(str.split())
while str != 'end':
    in_arr.append([int(i) for i in str.split()])
    str = input()
    n += 1
out_arr = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        for di in range(-1, 2, 2):
            in_arr_i = i + di
            if in_arr_i < 0:
                in_arr_i = n - 1
            if in_arr_i == n:
                in_arr_i = 0
            out_arr[i][j] += in_arr[in_arr_i][j]
        for dj in range(-1, 2, 2):
            in_arr_j = j + dj
            if in_arr_j < 0:
                in_arr_j = m - 1
            if in_arr_j == m:
                in_arr_j = 0
            out_arr[i][j] += in_arr[i][in_arr_j]
for i in range(n):
    for j in range(m):
        print(out_arr[i][j], end = ' ')
    print()