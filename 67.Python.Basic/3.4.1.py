with open('dataset_3363_2.txt') as infile:
    s = infile.readline().strip()
out = ''
tmp = []
for i in s:
    tmp.append(i)
l = len(tmp)
j = 0
for i in range(l):
    if i < l - j:
        if tmp[i].isdigit():
            if i != l - j - 1:
                if tmp[i + 1].isdigit():
                    tmp[i] += tmp[i + 1]
                    del tmp[i + 1]
                    j += 1
for i in range(0, len(tmp) - 1, 2):
    out += tmp[i] * int(tmp[i + 1])
with open('outfile.txt', 'w') as outfile:
    outfile.write(out + '\n')
