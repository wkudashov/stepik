import xml.etree.ElementTree as Xml


def calc(tree_element, result_dict, lvl=1):
    r = result_dict
    # print(f"Cost: {lvl}. item: {tree_element.attrib['color']}")
    r[tree_element.attrib['color']] += int(lvl)
    level = lvl + 1
    for child in tree_element:
        # print(f'Parent: {tree_element.attrib["color"]}')
        calc(child, r, level)


root = Xml.fromstring(input())

result = {'red': 0, 'green': 0, 'blue': 0}
calc(root, result)

print(result['red'], result['green'], result['blue'])
