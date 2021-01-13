a = []
with open('dataset_3363_3.txt') as infile:
    for i in infile:
        a += i.strip().lower().split()
word = a[0]
count = 1
for i in a:
    if a.count(i) > count:
        word = i
        count = a.count(i)
    elif a.count(i) == count and word > i:
        word = i
with open('outfile.txt', 'w') as outf:
    outf.write(word + ' ' + str(count) + '\n')
