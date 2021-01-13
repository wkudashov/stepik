import sys
import re

for line in sys.stdin:
    if re.search(r'\\', line):
        print(line.strip())
