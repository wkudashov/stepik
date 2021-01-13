with open('dataset_3380_5.txt') as inf:
    s = [i.strip().split('\t') for i in inf]
d = {i: [0, 0] for i in range(1, 12)}
for i in s:
    d[int(i[0])][0] += int(i[2])
    d[int(i[0])][1] += 1
for i in d.values():
    if i[0] == 0:
        i[0] = '-'
    else:
        i[0] = i[0] / i[1]
with open('outfile.txt', 'w') as ouf:
    for i in d.keys():
        ouf.write(str(i) + ' ' + str(d[i][0]) + '\n')
