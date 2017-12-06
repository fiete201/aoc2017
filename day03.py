#!/usr/bin/python3
import sys
from datetime import datetime
import time
import math

before = datetime.now()
with open(sys.argv[1], 'r') as f:
    iinput = int(f.read())
squarenumber = math.floor(math.sqrt(iinput))+1
squarenumber += (squarenumber+1) % 2
hsquarenumber = math.floor(squarenumber/2)
spiral=[[0] * squarenumber for i in range(squarenumber)]
spiral2=[[0] * squarenumber for i in range(squarenumber)]
x = hsquarenumber
y = hsquarenumber
n = 1
calc_adjsum = 1
result2 = 0

def calculate_adjacent_sum():
    adjacent_sum = 0
    global result2
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
        result2 = adjacent_sum
        calc_adjsum = 0
    return adjacent_sum

def draw_number():
    global n
    spiral[y][x] = n
    n += 1
    if (calc_adjsum == 1):
        spiral2[y][x] = calculate_adjacent_sum()

draw_number()
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

for s in range(squarenumber):
    for t in range(squarenumber):
        if (spiral[s][t] == iinput):
            result = math.fabs(hsquarenumber - s) + math.fabs(hsquarenumber - t)
after = datetime.now()
print('Solution 1:', result)
print('Solution 2:', result2)
print('Duration:', after-before)

#old solution for part01
#    distances = []
#    distances.append(0)
#    for i in range(4):
#        distances.append(1)
#        distances.append(2)
#        
#    for i in range(5, squarenumber+1, 2):
#        for l in range(4):
#            for j in range(i-2, math.floor(i/2), -1):
#                distances.append(j)
#            for k in range(math.floor(i/2), i):
#                distances.append(k)
