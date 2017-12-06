#!/usr/bin/python3
import sys
from datetime import datetime
import timeit

# Global variables
result01 = 0
result02 = 0
input = ''

#part 1
def part01():
    global result01
    global input
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
    result01 = sum


#part 2
def part02():
    global result02
    global input
    sum = 0
    i = 0
    l = len(input)
    while i < l:
        if (input[i] == input[int((i+(l/2))%l)]):                                   
            sum += int(input[i])
        i += 1
    result02 = sum


def bench(part=0, filename=''):
    global input
    input = ''
    if filename != '':
        with open(filename, 'r') as f:
           input = f.readline() 

        if part == 1:
            duration01 = timeit.timeit("part01()", setup="from day01 import part01", number=1)
            print(1, 1, result01, int(duration01 * 10 ** 6))
        elif part == 2:
            duration02 = timeit.timeit("part02()", setup="from day01 import part02", number=1)
            print(1, 2, result02, int(duration02 * 10 ** 6)) 
            

# Main
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        input = f.readline()

    duration01 = timeit.timeit("part01()", setup="from __main__ import part01", number=1)
    print(1, 1, result01, int(duration01 * 10 ** 6))

    duration02 = timeit.timeit("part02()", setup="from __main__ import part02", number=1)
    print(1, 2, result02, int(duration02 * 10 ** 6)) 

