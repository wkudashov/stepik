gen = input()
co_gen = ''
n = 1
for i in range(len(gen)):
    if i < len(gen) - 1:
        if gen[i] == gen[i + 1]:
            n += 1
        else:
            co_gen += gen[i] + str(n)
            n = 1
    else:
        co_gen += gen[i] + str(n)
print(co_gen)
