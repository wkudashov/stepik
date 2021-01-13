import requests
with open('dataset_3378_2.txt') as infile:
    url = infile.read().strip()
r = requests.get(url)
print(len(r.text.splitlines()))
