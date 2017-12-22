#!/usr/bin/python3
# Imports
import sys
from functools import partial
import timeit

# Global variables
jumplist = []
result01 = 0
result02 = 0

# Functions
def part01(jumplist=[]):
    #global jumplist
    global result01
    pc = 0
    maxpc = 0
    steps = 0
    maxpc = len(jumplist)
    pcv = jumplist[pc]
    while (pc < maxpc and pc > -1):
        oldpc = pc
        pcv = jumplist[pc]
        pc += pcv
        jumplist[oldpc] = pcv + 1
        steps += 1
    result01 = steps

def part02(jumplist=[]):
    #global jumplist
    global result02
    pc = 0
    steps = 0
    maxpc = len(jumplist)
    pcv = jumplist[pc]
    while (pc < maxpc and pc > -1):
        oldpc = pc
        pcv = jumplist[pc]
        pc += pcv
        if (pcv > 2):
            jumplist[oldpc] = pcv - 1
        else:
            jumplist[oldpc] = pcv + 1
        steps += 1
    result02 = steps

def bench(part=0, filename=''):
    global jumplist
    if filename != '':
        with open(filename, 'r') as f:
            for line in f:
                jumplist.append(int(line))
        if part == 1:
            duration01 = timeit.timeit(partial(part01, jumplist.copy()), setup="from day05 import part01", number=1)
            print(5, 1, result01, int(duration01 * 10 ** 6))
        elif part == 2:
            duration02 = timeit.timeit(partial (part02, jumplist.copy()), setup="from day05 import part02", number=1)
            print(5, 2, result02, int(duration02 * 10 ** 6)) 
            

# Main
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            jumplist.append(int(line))

    duration01 = timeit.timeit(partial(part01, jumplist.copy()), setup="from __main__ import part01", number=1)
    print(5, 1, result01, int(duration01 * 10 ** 6))

    duration02 = timeit.timeit(partial(part02, jumplist.copy()), setup="from __main__ import part02", number=1)
    print(5, 2, result02, int(duration02 * 10 ** 6)) 
