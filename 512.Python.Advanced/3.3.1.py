import requests
import re

source = requests.get(input().strip())
target_url = input().strip()

urls = []
step_status = False

if source.status_code == 200:
    urls = re.findall(r'href="(.+?)"', source.text)

for url in urls:
    page = requests.get(url)
    if page.status_code == 200:
        if target_url in page.text:
            step_status = True

print('Yes' if step_status else 'No')
