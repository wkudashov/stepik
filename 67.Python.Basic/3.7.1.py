n = int(input())
m = []
for i in range(n):
    m.append(input().strip().split(';'))
board = {}
print(m)
for i in range(n):
    # Заменяем счет в матче на очки, полученные командами
    if m[i][1] > m[i][3]:
        m[i][1], m[i][3] = 3, 0
    elif m[i][1] == m[i][3]:
        m[i][1], m[i][3] = 1, 1
    else:
        m[i][1], m[i][3] = 0, 3
    # Создаем словарь. Ключ - команда, элемент - список. Первый элемент списка - количество матчей
    if m[i][0] not in board:
        board[m[i][0]] = [1, 0, 0, 0, 0]
    #    print(board[m[i][0]][4])
    else:
        board[m[i][0]][0] += 1
    #    print(board[m[i][0]][4])
    if m[i][2] not in board:
        board[m[i][2]] = [1, 0, 0, 0, 0]
    #    print(board[m[i][2]][4])
    else:
        board[m[i][2]][0] += 1
    #    print(board[m[i][2]][4])
    # Добавляем в словарь по ключу количество побед, поражений и ничьих
    if m[i][1] == 3:
        board[m[i][0]][1] += 1
    elif m[i][1] == 1:
        board[m[i][0]][2] += 1
    else:
        board[m[i][0]][3] += 1
    board[m[i][0]][4] += m[i][1]
    if m[i][3] == 3:
        board[m[i][2]][1] += 1
    elif m[i][3] == 1:
        board[m[i][2]][2] += 1
    else:
        board[m[i][2]][3] += 1
    board[m[i][2]][4] += m[i][3]
# Выводим результат
for i in board:
    print(i, end=':')
    for j in range(len(board[i])):
        print(board[i][j], end=' ')
    print()
