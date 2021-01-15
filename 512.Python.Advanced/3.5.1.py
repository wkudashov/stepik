import requests

with open('dataset_24476_3.txt', 'r') as in_file, open('result.txt', 'w') as out_file:
    for number in in_file.readlines():
        response = requests.get('http://numbersapi.com/' + number.strip() + '/math', params={'json': True})
        print('writing', response.json()['number'], response.json()['found'])
        out_file.write('Interesting\n' if response.json()['found'] else 'Boring\n')
