nd = int(input())
d = []
for i in range(nd):
    d.append(input().lower())
nl = int(input())
l = []
for i in range(nl):
    l.append(input().lower().split())
err = []
for i in l:
    for j in i:
        if j not in d and j not in err:
            err.append(j)
for i in err:
    print(i)
