#!/usr/bin/python3
import sys
from datetime import datetime
import time

before = datetime.now()
sum = 0
with open(sys.argv[1], 'r') as f:
    for line in f:
        pwline = line.rstrip().split(' ')
        unique_pw = set()
        for pw in pwline:
            pw = ''.join(sorted(pw))
            unique_pw.add(pw)
        if (len(pwline) == len(unique_pw)):
            sum += 1
after = datetime.now()
print('Solution 1:', sum)
print('Duration:', after-before)
