s = 0
if len(objects) > 0:
    s = len(objects)
    for i in range(len(objects)):
        a = 0
        for j in range(i + 1, len(objects)):
            if i+1 < len(objects) and objects[i] is objects[j]:
                a += 1
        if a != 0:
            s -= 1
print(s)
