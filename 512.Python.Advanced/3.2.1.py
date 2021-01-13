import sys
import re

for line in sys.stdin:
    if len(re.findall(r'cat', line)) > 1:
        print(line.strip())
