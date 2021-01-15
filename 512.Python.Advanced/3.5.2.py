import requests
import json

params = {
    'client_id': '0a4aafd4e8c0789c449d',
    'client_secret': '78853bdf384c1e8d4804d41903c60732'
}

res = requests.post('https://api.artsy.net/api/tokens/xapp_token', data=params)
token = res.json()['token']

header = {'X-Xapp-Token': token}

artists = {}

with open('dataset_24476_4.txt', 'r', encoding='utf-8') as in_file:
    for art_id in in_file.readlines():
        response = requests.get("https://api.artsy.net/api/artists/" + art_id.strip(), headers=header)
        name = response.json()['sortable_name']
        date = response.json()['birthday']
        print('reading', name, date)
        if date in artists.keys():
             artists[date].append(name)
        else:
            artists[date] = [name]

keys = list(artists.keys())
keys.sort()

with open('result.txt', 'w', encoding='utf-8') as out_file:
    for d in keys:
        artists[d].sort()
        for n in artists[d]:
            print('writing', d, n)
            out_file.write(n + '\n')
