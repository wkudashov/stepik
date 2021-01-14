import re
import requests

sites = []
urls = []

link = input().strip()
file = requests.get(link)

if file.status_code == 200:
    urls = re.findall(r'<a.*?href=[\"\']?(?:.*?://)?(\w[\w\-.]*)', file.text)

output = list(set(urls))
output.sort()

for url in output:
    print(url)
