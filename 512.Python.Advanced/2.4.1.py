with open(".txt", "r") as _input:
    lst = _input.read().splitlines()

with open("reverse.txt", "w") as _output:
    for i in lst[::-1]:
        _output.write(i+"\n")
