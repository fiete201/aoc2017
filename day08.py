#!/usr/bin/python3
import sys
from datetime import datetime
import timeit

# Global variables
instructions = []
registers = dict()
result01 = 0
result02 = 0

# Functions
def part01():
    global registers
    global instructions
    global result01
    sum = 0
    for instruction in instructions:
        # create register if needed
        if instruction[0] not in registers:
            registers[instruction[0]] = 0
        if instruction[4] not in registers:
            registers[instruction[4]] = 0

        # determine condition and check
        if instruction[5] == '<':
            if registers[instruction[4]] < int(instruction[6]):
                calculateInstruction(instruction[1], instruction[0], int(instruction[2]))
        elif instruction[5] == '<=':
            if registers[instruction[4]] <= int(instruction[6]):
                calculateInstruction(instruction[1], instruction[0], int(instruction[2]))
        elif instruction[5] == '==':
            if registers[instruction[4]] == int(instruction[6]):
                calculateInstruction(instruction[1], instruction[0], int(instruction[2]))
        elif instruction[5] == '>':
            if registers[instruction[4]] > int(instruction[6]):
                calculateInstruction(instruction[1], instruction[0], int(instruction[2]))
        elif instruction[5] == '>=':
            if registers[instruction[4]] >= int(instruction[6]):
                calculateInstruction(instruction[1], instruction[0], int(instruction[2]))
        elif instruction[5] == '!=':
            if registers[instruction[4]] != int(instruction[6]):
                calculateInstruction(instruction[1], instruction[0], int(instruction[2]))
        else:
            print('Unknown Instruction:', instruction[5])
            return

    result01=(max(registers.values()))
    
def calculateInstruction(operator='', register='', value=0):
    global registers
    global result02
    if operator == 'inc':
        registers[register] += value
    elif operator == 'dec':
        registers[register] -= value
    else:
        print ('Unknown Operator:', operator)

def part02():
    global registers
    global instructions
    global result02
    for instruction in instructions:
        # create register if needed
        if instruction[0] not in registers:
            registers[instruction[0]] = 0
        if instruction[4] not in registers:
            registers[instruction[4]] = 0

        # determine condition and check
        if instruction[5] == '<':
            if registers[instruction[4]] < int(instruction[6]):
                calculateInstruction(instruction[1], instruction[0], int(instruction[2]))
        elif instruction[5] == '<=':
            if registers[instruction[4]] <= int(instruction[6]):
                calculateInstruction(instruction[1], instruction[0], int(instruction[2]))
        elif instruction[5] == '==':
            if registers[instruction[4]] == int(instruction[6]):
                calculateInstruction(instruction[1], instruction[0], int(instruction[2]))
        elif instruction[5] == '>':
            if registers[instruction[4]] > int(instruction[6]):
                calculateInstruction(instruction[1], instruction[0], int(instruction[2]))
        elif instruction[5] == '>=':
            if registers[instruction[4]] >= int(instruction[6]):
                calculateInstruction(instruction[1], instruction[0], int(instruction[2]))
        elif instruction[5] == '!=':
            if registers[instruction[4]] != int(instruction[6]):
                calculateInstruction(instruction[1], instruction[0], int(instruction[2]))
        else:
            print('Unknown Instruction:', instruction[5])
            return

        if registers[instruction[0]] > result02:
            result02 = registers[instruction[0]]

def bench(part=0, filename=''):
    global instructions
    instructions = []
    if filename != '':
        with open(filename, 'r') as f:
            for line in f:
                instructions.append(line.rstrip().split(' '))
        if part == 1:
            duration01 = timeit.timeit("part01()", setup="from day08 import part01", number=1)
            print(8, 1, result01, int(duration01 * 10 ** 6))
        elif part == 2:
            registers = dict()
            duration02 = timeit.timeit("part02()", setup="from day08 import part02", number=1)
            print(8, 2, result02, int(duration02 * 10 ** 6)) 
            

# Main
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            instructions.append(line.rstrip().split(' '))

    duration01 = timeit.timeit("part01()", setup="from __main__ import part01", number=1)
    print(8, 1, result01, int(duration01 * 10 ** 6))

    registers = dict()
    duration02 = timeit.timeit("part02()", setup="from __main__ import part02", number=1)
    print(8, 2, result02, int(duration02 * 10 ** 6)) 
