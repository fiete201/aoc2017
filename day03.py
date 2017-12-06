#!/usr/bin/python3
import sys
from datetime import datetime
import timeit
import math

result01 = 0
result02 = 0
squarenumber = 0
hsquarenumber = 0
spiral = []
spiral2 = []
x = 0
y = 0
n = 0
calc_adjsum = 0

#old solution for part01
def part01():
    global result01
    global iinput
    squarenumber = math.floor(math.sqrt(iinput))+1
    squarenumber += (squarenumber+1) % 2
    distances = []
    distances.append(0)
    for i in range(4):
        distances.append(1)
        distances.append(2)
        
    for i in range(5, squarenumber+1, 2):
        for l in range(4):
            for j in range(i-2, math.floor(i/2), -1):
                distances.append(j)
            for k in range(math.floor(i/2), i):
                distances.append(k)
    result01 = distances[iinput]-1

def calculate_adjacent_sum():
    global result02
    global spiral2
    global iinput
    global x
    global y
    global squarenumber
    adjacent_sum = 0
    global calc_adjsum

    if (y > 0):
        adjacent_sum += spiral2[y-1][x] 
        if (x > 0):
            adjacent_sum += spiral2[y-1][x-1]
        if (x < squarenumber-1):
            adjacent_sum += spiral2[y-1][x+1]
    if (y < squarenumber-1):
        adjacent_sum += spiral2[y+1][x]
        if (x > 0):
            adjacent_sum += spiral2[y+1][x-1]
        if (x < squarenumber-1):
            adjacent_sum += spiral2[y+1][x+1]
    if (x > 0):
        adjacent_sum += spiral2[y][x-1]
    if (x < squarenumber-1):
        adjacent_sum += spiral2[y][x+1]
    if (adjacent_sum > iinput):
        result02 = adjacent_sum
        calc_adjsum = 0
    return adjacent_sum

def draw_number():
    global calc_adjsum
    global n
    #global spiral
    global spiral2
    global x
    global y
    #n = 1

    #spiral[y][x] = n
    #n += 1
    if (calc_adjsum == 1):
        spiral2[y][x] = calculate_adjacent_sum()

def part02():
    global x
    global y
    global calc_adjsum
    global spiral2
    global squarenumber
    squarenumber = math.floor(math.sqrt(iinput))+1
    squarenumber += (squarenumber+1) % 2
    hsquarenumber = math.floor(squarenumber/2)
    x = hsquarenumber
    y = hsquarenumber
    calc_adjsum = 1
    #spiral=[[0] * squarenumber for i in range(squarenumber)]
    spiral2=[[0] * squarenumber for i in range(squarenumber)]
    #draw_number()
    spiral2[y][x] = 1
    
    for i in range(3, squarenumber+1, 2):
        x += 1
        draw_number()
        for j in range(i-2):
            y -= 1
            draw_number()
        for k in range(i-1):
            x -= 1
            draw_number()
        for l in range(i-1):
            y += 1
            draw_number()
        for m in range(i-1):
            x += 1
            draw_number()
    
#    for s in range(squarenumber):
#        for t in range(squarenumber):
#            if (spiral[s][t] == iinput):
#                result = math.fabs(hsquarenumber - s) + math.fabs(hsquarenumber - t)

def bench(part=0, filename=''):
    global iinput
    global result01
    global result02
    iinput = 0
    if filename != '':
        with open(filename, 'r') as f:
            iinput = int(f.read())

        if part == 1:
            duration01 = timeit.timeit("part01()", setup="from day03 import part01", number=1)
            print(3, 1, result01, int(duration01 * 10 ** 6))
        elif part == 2:
            duration02 = timeit.timeit("part02()", setup="from day03 import part02", number=1)
            print(3, 2, result02, int(duration02 * 10 ** 6)) 
            

# Main
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        iinput = int(f.read())

    duration01 = timeit.timeit("part01()", setup="from __main__ import part01", number=1)
    print(3, 1, result01, int(duration01 * 10 ** 6))

    duration02 = timeit.timeit("part02()", setup="from __main__ import part02", number=1)
    print(3, 2, result02, int(duration02 * 10 ** 6)) 
