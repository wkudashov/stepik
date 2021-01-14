import json

raw_data = json.loads(input())
data = {}
result = {}

for item in raw_data:
    data[item['name']] = item['parents']
    result[item['name']] = 0


def checker(ch, pa):
    return ch == pa or any(map(lambda i: checker(ch, i), data[pa]))


for item in result.keys():
    for test in data.keys():
        if checker(item, test):
            result[item] += 1

klist = list(result.keys())
klist.sort()

for i in klist:
    print(f'{i} : {result[i]}')
