import tempfile
import requests
import xmltodict

url = 'https://stepik.org/media/attachments/lesson/245681/map2.osm'
counter = 0

with tempfile.TemporaryFile() as tmp_file:
    osm_map = requests.get(url, stream=True)
    n = 0
    for chunk in osm_map.iter_content(chunk_size=128):
        print('\r', end='')
        tmp_file.write(chunk)
        print(f'Saved {128*n} bytes', end='')
        n += 1
    print()
    tmp_file.seek(0)
    parsedxml = xmltodict.parse(tmp_file)

for smth in parsedxml['osm'].keys():
    if isinstance(parsedxml['osm'][smth], list):
        for smth_item in parsedxml['osm'][smth]:
            if 'tag' in smth_item.keys():
                if isinstance(smth_item['tag'], list):
                    for tag_item in smth_item['tag']:
                        if 'fuel' in tag_item.values():
                            counter += 1
                else:
                    if 'fuel' in smth_item['tag'].values():
                        counter += 1

print(counter)

