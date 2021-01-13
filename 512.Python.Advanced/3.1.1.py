st = input()
case = input()
t = input()
count = 0

if st.find(case) == -1:
    print(0)
else:
    while st.replace(case, t) != st and count <= 1000:
        st = st.replace(case, t)
        count += 1
    if 0 < count <= 1000:
        print(count)
    else:
        print('Impossible')
