import sys
import re

for line in sys.stdin:
    if re.search(r'\bcat\b', line):
        print(line.strip())
