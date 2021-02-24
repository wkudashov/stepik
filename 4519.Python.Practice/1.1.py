from urllib.request import urlopen

html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')

c = html.lower().count('c++')
p = html.lower().count('python')
if c > p:
    print(f'c++ {c}')
elif c == p:
    print('equally')
else:
    print(f'python {p}')
