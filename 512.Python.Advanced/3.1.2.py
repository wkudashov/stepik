st = input()
case = input()
counter = 0
pos = st.find(case)

if pos == -1:
    print(0)
else:
    while pos != -1:
        pos = st.find(case, pos + 1)
        counter += 1
    print(counter)
