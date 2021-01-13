a = []
with open('dataset_3363_4.txt') as infile:
    for i in infile:
        a.append(i.strip().split(';'))
b = []
math = 0
phis = 0
lang = 0
for i in range(len(a)):
    b.append((int(a[i][1]) + int(a[i][2]) + int(a[i][3])) / 3)
    math += int(a[i][1])
    phis += int(a[i][2])
    lang += int(a[i][3])
b.append(str(math / len(a)) + ' ' + str(phis / len(a)) + ' ' + str(lang / len(a)))
with open('outfile.txt', 'w') as outfile:
    for i in range(len(b)):
        outfile.write(str(b[i]) + '\n')
