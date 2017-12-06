#!/usr/bin/python3
import sys
from datetime import datetime
import timeit

# Global variables
pwlist = []
result01 = 0
result02 = 0

# Functions
def part01():
    global pwlist
    global result01
    sum = 0
    for pwline in pwlist:
        unique_pw = set()
        for pw in pwline:
            unique_pw.add(pw)
        if (len(pwline) == len(unique_pw)):
            sum += 1
    result01 = sum

def part02():
    global pwlist
    global result02
    sum = 0
    for pwline in pwlist:
        unique_pw = set()
        for pw in pwline:
            pw = ''.join(sorted(pw))
            unique_pw.add(pw)
        if (len(pwline) == len(unique_pw)):
            sum += 1
    result02 = sum

def bench(part=0, filename=''):
    global pwlist
    pwlist = []
    if filename != '':
        with open(filename, 'r') as f:
            for line in f:
                pwlist.append(line.rstrip().split(' '))
        if part == 1:
            duration01 = timeit.timeit("part01()", setup="from day04 import part01", number=1)
            print(4, 1, result01, int(duration01 * 10 ** 6))
        elif part == 2:
            duration02 = timeit.timeit("part02()", setup="from day04 import part02", number=1)
            print(4, 2, result02, int(duration02 * 10 ** 6)) 
            

# Main
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            pwlist.append(line.rstrip().split(' '))

    duration01 = timeit.timeit("part01()", setup="from __main__ import part01", number=1)
    print(4, 1, result01, int(duration01 * 10 ** 6))

    duration02 = timeit.timeit("part02()", setup="from __main__ import part02", number=1)
    print(4, 2, result02, int(duration02 * 10 ** 6)) 
