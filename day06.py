#!/usr/bin/python3
import sys
from datetime import datetime
import time
import timeit

# Global variables
iterations = 0
loop_detected = 0
memorybanks = []
oldinput = []
numberofbanks = 0
result01 = 0
result02 = 0
loop_index_start = 0

# Functions
def part01():
    global numberofbanks
    global memorybanks
    global result01
    loop_detected = 0
    oldinput = []
    iterations = 0
    numberofbanks = len(memorybanks)
    while loop_detected == 0:
        oldinput.append(list(memorybanks))
        maxval = 0
        maxindex = 0
        interim = 0
        i = 0
        while i < numberofbanks:
            if memorybanks[i] > maxval:
                maxval = memorybanks[i]
                maxindex = i
            i += 1
        interim = memorybanks[maxindex]
        memorybanks[maxindex] = 0
        j = maxindex + 1
        while interim > 0:
            memorybanks[j%numberofbanks] += 1
            interim -= 1
            j += 1
       # for oldbanks in oldinput:
       #     if (memorybanks == oldbanks):
       #         loop_detected = 1
        if memorybanks in oldinput:
            loop_detected = 1
        iterations += 1
    result01 = iterations

def part02():
    global memorybanks
    global numberofbanks
    global result02
    loop_detected = 0
    oldinput = []
    iterations = 0
    loop_index_start = 0
    numberofbanks = len(memorybanks)
    while loop_detected == 0:
        oldinput.append(list(memorybanks))
        maxval = 0
        maxindex = 0
        interim = 0
        i = 0
        while i < numberofbanks:
            if memorybanks[i] > maxval:
                maxval = memorybanks[i]
                maxindex = i
            i += 1
        interim = memorybanks[maxindex]
        memorybanks[maxindex] = 0
        j = maxindex + 1
        while interim > 0:
            memorybanks[j%numberofbanks] += 1
            interim -= 1
            j += 1
        k = 0
        #kmax = len(oldinput)
#        while k < iterations + 1:
#            if (memorybanks == oldinput[k]):
#                loop_detected = 1
#                loop_index_start = k
#            k += 1
        if memorybanks in oldinput:
            loop_detected = 1
            loop_index_start = oldinput.index(memorybanks) 
 
        iterations += 1
    result02 = iterations - loop_index_start

def bench(part=0, filename=''):
    global memorybanks
    memorybanks = []
    if filename != '':
        with open(filename, 'r') as f:
            line = f.readline()
        for element in line.split('\t'):
            memorybanks.append(int(element))
        if part == 1:
            duration01 = timeit.timeit("part01()", setup="from day06 import part01", number=1)
            print(6, 1, result01, int(duration01 * 10 ** 6)) 
        else:
            duration02 = timeit.timeit("part02()", setup="from day06 import part02", number=1)
            print(6, 2, result02, int(duration02 * 10 ** 6)) 
    
# Main
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        line = f.readline()
    for element in line.split('\t'):
        memorybanks.append(int(element))

    duration01 = timeit.timeit("part01()", setup="from __main__ import part01", number=1)
    print(6, 1, result01, int(duration01 * 10 ** 6)) 
    duration02 = timeit.timeit("part02()", setup="from __main__ import part02", number=1)
    print(6, 2, result02, int(duration02 * 10 ** 6)) 
