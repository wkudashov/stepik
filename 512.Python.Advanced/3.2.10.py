import sys
import re

for line in sys.stdin:
    if re.fullmatch(r'[01]+', line.strip()) and re.fullmatch(r'0*((1(01*0)*1)*0*)*', line.strip()):
        print(line.strip())
