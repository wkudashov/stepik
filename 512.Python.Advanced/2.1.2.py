relation_count = int(input())
parents = {}

for _ in range(relation_count):
    query = input().split()
    parents[query[0]] = [] if len(query) == 1 else query[2:]

exceptions_count = int(input())
exceptions = []


def is_parent(child, parent):
    return child == parent or any(map(lambda item: is_parent(item, parent), parents[child]))

print(parents)
for i in range(exceptions_count):
    exceptions.append(input())
    print('searching ', exceptions[i], 'parents in ', exceptions[:i])
    if any(map(lambda item: is_parent(exceptions[i], item), exceptions[:i])):
        print(exceptions[i])
