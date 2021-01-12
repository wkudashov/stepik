lst = []

with open(file.txt, "r") as _input:
    for i in _input:
        lst = _input.readline()

with open(reverse.txt, "w") as _output:
    for i in lst.reverse():
        _output.write(i)
