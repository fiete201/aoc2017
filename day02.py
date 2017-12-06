#!/usr/bin/python3
import sys
from datetime import datetime
import time

before = datetime.now()
sum = 0
with open(sys.argv[1], 'r') as f:
    for line in f:
        lowest = 0
        highest = 0
        spreadline = line.split('\t')
        for number in spreadline:
            inumber = int(number)
            if (lowest == 0 and highest == 0):
                highest = inumber
                lowest = inumber
            elif (inumber > highest):
                highest = inumber
            elif (inumber < lowest):
                lowest = inumber
        
        sum += highest - lowest
after = datetime.now()
print('Solution 1:', sum)
print('Duration:', after-before)

before = datetime.now()
sum = 0
with open(sys.argv[1], 'r') as f:
    for line in f:
        spreadline = line.split('\t')
        l = len(spreadline)
        i = 0
        while i < l:
            inumber = int(spreadline[i])
            k = i + 1
            while k < l:
                knumber = int(spreadline[k])
                if (inumber % knumber == 0):
                    sum += inumber / knumber
                    k = l
                    i = l
                elif (knumber % inumber == 0):
                    sum += knumber / inumber
                    k = l
                    i = l
                else:
                    k += 1
            i += 1

after = datetime.now()
print('Solution 2:', sum)
print('Duration:', after-before)
