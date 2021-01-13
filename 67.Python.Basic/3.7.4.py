d = {'север': 0, 'юг': 0, 'восток': 0, 'запад': 0}
n = [input().lower().split() for i in range(int(input()))]
for i in n:
    d[i[0]] += int(i[1])
print(d['восток'] - d['запад'], d['север'] - d['юг'])
