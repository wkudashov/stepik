import requests
with open('dataset_3378_3.txt') as file1:
    url = file1.read().split()
words = []
i = 0
pre = 'https://stepic.org/media/attachments/course67/3.6.3/'

while url[i][len(pre)] + url[i][len(pre) + 1] != 'We':
    words.append(requests.get(url[i]).text.strip())
    url.append(pre + words[i])
    print(url[i])
    print(url[i][len(pre)] + url[i][len(pre) + 1])
    i += 1

with open('outfile.txt', 'w') as ouf:
    ouf.write(requests.get(url[i-1]).text)
