kin, kout, sin1, sin2 = input(), input(), input(), input()
sout1, sout2 = [], []
for i in range(len(sin1)):
    for j in range(len(kin)):
        if sin1[i] == kin[j]:
            sout1.append(kout[j])
for i in range(len(sin2)):
    for j in range(len(kout)):
        if sin2[i] == kout[j]:
            sout2.append(kin[j])
for i in sout1:
    print(i, end='')
print()
for i in sout2:
    print(i, end='')

