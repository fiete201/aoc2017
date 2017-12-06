#!/usr/bin/python3
import sys
from datetime import datetime
import timeit

spreadlist = []

def part01():
    global spreadlist
    global result01
    sum = 0
    for spreadline in spreadlist:
        lowest = 0
        highest = 0
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
    result01 = sum

def part02():
    global spreadlist
    global result02
    sum = 0
    for spreadline in spreadlist:
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
    result02 = int(sum)

def bench(part=0, filename=''):
    global spreadlist
    spreadlist = []
    if filename != '':
        with open(filename, 'r') as f:
            for line in f:
                spreadlist.append(line.split('\t'))

        if part == 1:
            duration01 = timeit.timeit("part01()", setup="from day02 import part01", number=1)
            print(2, 1, result01, int(duration01 * 10 ** 6))
        elif part == 2:
            duration02 = timeit.timeit("part02()", setup="from day02 import part02", number=1)
            print(2, 2, result02, int(duration02 * 10 ** 6)) 
            

# Main
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            spreadlist.append(line.split('\t'))

    duration01 = timeit.timeit("part01()", setup="from __main__ import part01", number=1)
    print(2, 1, result01, int(duration01 * 10 ** 6))

    duration02 = timeit.timeit("part02()", setup="from __main__ import part02", number=1)
    print(2, 2, result02, int(duration02 * 10 ** 6)) 

