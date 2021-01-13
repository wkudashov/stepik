import sys
import re

for line in sys.stdin:
    if re.search(r'\b(\w+)\1\b', line):
        print(line.strip())
