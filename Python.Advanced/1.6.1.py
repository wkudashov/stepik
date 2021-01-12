classes = {}
query = []


def parent_check(is_parent, is_child):
    global classes
    if is_parent == is_child:
#        print('is_parent == is_child', is_parent, is_child)
        return True
    elif is_child in classes.keys():
#        print('is_child in classes.keys()', is_child, classes.keys())
        if is_parent in classes[is_child]:
#            print('is_parent in classes[is_child]', is_parent, classes[is_child])
            return True
        else:
#            print('is_child NOT in classes[is_parent]', is_parent, classes[is_child])
            if classes[is_child] != []:
                for i in classes[is_child]:
#                    print('recursive check parent', i)
                    if parent_check(is_parent, i):
                        return True
            else:
#                print('У класса ', is_child, 'нет родителей', classes[is_child])
                return False
    else:
        return False


count_classes = int(input())
for _ in range(count_classes):
    _class = input().split()
    classes[_class[0]] = []
    if len(_class) > 2:
        classes[_class[0]] += _class[2:]
    print(_class)

count_queries = int(input())
for _ in range(count_queries):
    query = input().split()
#    print('запрос', query[0], query[1])
    if parent_check(query[0], query[1]):
        print('Yes')
    else:
        print('No')
