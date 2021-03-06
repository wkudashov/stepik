import xmltodict

tag_count = 0
tagless_count = 0
all = 0

with open('map2.osm', 'r', encoding='utf-8') as fin:
    file = fin.read()
    parsedxml = xmltodict.parse(file)
    for node in parsedxml['osm']['node']:
        all += 1
        if 'tag' in node.keys():
            tag_count += 1
            # print('TAG', tag_count, node.keys())
        else:
            tagless_count += 1
            # print('NO TAG', tagless_count, node.keys())

print(tag_count, tagless_count)
