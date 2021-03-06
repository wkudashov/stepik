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

for node in parsedxml['osm']['node']:
    if 'tag' in node.keys():
        if isinstance(node['tag'], list):
            for tag_item in node['tag']:
                if 'fuel' in tag_item.values():
                    counter += 1
        else:
            if 'fuel' in node['tag'].values():
                counter += 1

print(counter)

