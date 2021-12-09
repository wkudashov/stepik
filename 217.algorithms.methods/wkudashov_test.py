from sys import argv
from os import path

# reading and checking script parameters. expecting two filenames of existing files
filename1, filename2 = '', ''
if len(argv) > 2:
    filename1 = argv[1]
    if not path.isfile(filename1):
        exit(f'file {filename1} does not exist')
    filename2 = argv[2]
    if not path.isfile(filename2):
        exit(f'file {filename2} does not exist')
else:
    exit('file names are not specified in the script parameters')

arr1 = []
arr2 = []
result = []

# reading files into arr1 and arr1 arrays. splitting lines by '=' symbol for defining configuration file
with open(filename1) as f1, open(filename2) as f2:
    for line in f1:
        arr1.append(line.rstrip().split('='))
    for line in f2:
        arr2.append(line.rstrip().split('='))

# checking arrays length
if len(arr1) == 0 or len(arr2) == 0:
    exit('empty file specified')

# renaming arrays if needed. arr1 for text data, arr2 for config data
if len(arr1[0]) == 2:
    arr1, arr2 = arr2, arr1

# replacing substrings, counting symbols replaced
for item1 in arr1:
    # appending counter to the line
    item1.append(0)
    for item2 in arr2:
        if len(item2) != 2 or item2[0] == '':
            exit(f'bad configuration file schema. detected string {item2}')
        # for each rule in config file incrementing counter by total symbols in replaced substrings
        item1[1] += item1[0].count(item2[0])*len(item2[0])
        # and replacing substring
        item1[0] = item1[0].replace(item2[0], item2[1])
    # appending changed line and symbols counter to the result array
    result.append([item1[1], item1[0]])

# output changed lines in sorted by number of replaced symbols order
for i in sorted(result, reverse=True):
    print(i[1])
