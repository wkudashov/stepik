from urllib.request import urlopen
import re

html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
untagged = re.findall(r'<code>(.*?)</code>', html)

result = {}

for i in untagged:
    if untagged.count(i) not in result.keys():
        result[untagged.count(i)] = set()
    result[untagged.count(i)].add(i)

print(*sorted(result[max(result.keys())]))
