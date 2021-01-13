import sys
import re

for line in sys.stdin:
    if re.search(r'z...z', line):
        print(line.strip())
