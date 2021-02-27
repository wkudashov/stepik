from urllib.request import urlopen
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/5.html')
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html5lib')
total = 0
for i in soup.find_all('td'):
    total += int(i.string)
print(total)
# for i in soup.find_all('tr'):
#     for j in i.find_all('td'):
#         print(j.string, end=' ')
#     print('')