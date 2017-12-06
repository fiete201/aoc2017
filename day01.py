#!/usr/bin/python3
import sys
from datetime import datetime
import time

before = datetime.now()
with open(sys.argv[1], 'r') as f:
    input = f.read()

#part 1
sum = 0
i = 0
while i < len(input):
    if (i < len(input) - 1):
        if (input[i] == input[i+1]):
            sum += int(input[i])
    else:
        if (input[i] == input[0]):
            sum += int(input[i])
    i += 1
after = datetime.now()
print('Solution 1:', sum)
print('Duration:', after-before)

#part 2
#sum = 0
#i = 0
#l = len(input)
#while i < l:
#    if (input[i] == input[int((i+(l/2))%l)]):                                   
#        sum += int(input[i])
#    i += 1
#print('Solution 2:', sum)
