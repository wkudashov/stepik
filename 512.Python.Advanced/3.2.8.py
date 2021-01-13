import sys
import re

for line in sys.stdin:
    print(re.sub(r'\b(\w)(\w)', r'\2\1', line.strip()))
