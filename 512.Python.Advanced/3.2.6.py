import sys
import re

for line in sys.stdin:
    print(re.sub('human', 'computer', line.strip()))
