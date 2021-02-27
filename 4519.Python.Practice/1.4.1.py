from urllib.request import urlopen
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html')
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')
total = 0
for i in soup.find_all('td'):
    total += int(i.get_text())
print(total)
