n = int(input())
namespaces = {'global': 'None'}
variables = {'global': []}

for i in range(n):
    query = input().split()
    if query[0] == 'create':
        namespaces[query[1]] = query[2]
        variables[query[1]] = []
    elif query[0] == 'add':
        if query[1] in variables.keys():
            variables[query[1]].append(query[2])
    elif query[0] == 'get':
        current_ns = query[1]
        while current_ns != 'None':
            if current_ns not in namespaces.keys():
                current_ns = 'None'
                break
            if query[2] in variables[current_ns]:
                break
            else:
                current_ns = namespaces[current_ns]
        print(current_ns)
