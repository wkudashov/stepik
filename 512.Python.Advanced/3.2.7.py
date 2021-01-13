import sys
import re

for line in sys.stdin:
    print(re.sub(r'\b[aA]+\b', 'argh', line.strip(), count=1))
