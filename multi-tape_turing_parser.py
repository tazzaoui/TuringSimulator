#!/usr/bin/env python3

import sys

def print_tapes(tapes):
    for i in range(len(tapes)):
        print_tape(tapes, i)

def print_tape(tapes, tape):
    for i in tapes[tape]:
        sys.stdout.write("[{}]".format(i))
    print('')

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    exit(1)

input_file = list()
tapes = list(list())
heads = list()
tape_count = 0
line_number = 0

with open(sys.argv[1], 'r') as f:
    input_file = f.readlines()

print("Reading {}...".format(sys.argv[1]))
print("Read in {} instructions...\n".format(len(input_file)))

tape_line = input_file[line_number]

while(tape_line.split(' ')[0][:4] == "tape"):
    t = input_file[line_number].split(' ')[2].strip('\n')
    while(len(tapes) <= tape_count):
        tapes.append(list())
    for i in range(len(t)):
        tapes[line_number].append(t[i])
    heads.append(0)
    heads[line_number] = 0
    line_number += 1
    tape_line = input_file[line_number]
    tape_count += 1

while input_file[line_number] != "done":
    line = input_file[line_number]
    line_split = line.split(" ")
    if line_split[0] == "move":
        tape = int(line_split[1])
        direction = line_split[2].split("\n")[0]
        if direction == "RIGHT":
            heads[int(tape)] += 1
        elif direction == "LEFT":
            if(heads[int(tape)] > 0):
                heads[int(tape)] -= 1
        elif direction == "END":
            heads[int(tape)] = len(tapes[tape]) - 1
        elif direction == "START":
            heads[int(tape)] = 0
        else:
            print("ERROR ON LINE {}. No such direction: {}".format(line_number,direction))
            exit(1)
    elif line_split[0] == "moveto":
        tape = int(line_split[1])
        target = line_split[2].strip('\n')
        for i in range(heads[tape], len(tapes[tape])):
            if(tapes[tape][i] == target):
                heads[tape] = i
                break
    elif line_split[0] == "movebackto":
        tape = int(line_split[1])
        target = line_split[2].strip('\n')
        i = len(tapes[tape]) - 1
        while(i >= 0):
            if(tapes[tape][i] == target):
                heads[tape] = i
                break
            i -= 1
    elif line_split[0] == "if":
        tape = int(line_split[1])
        if(tapes[tape][heads[tape]] == line_split[2]):
            direction = line_split[3].strip('\n')
            if direction == "RIGHT":
                heads[tape] += 1
            elif direction == "LEFT":
                if(heads[tape] > 0):
                    heads[tape] -= 1
            elif direction == "WRITE":
                if(heads[tape] >= len(tapes[tape])):
                    tapes[tape].append(line_split[4].strip('\n'))
                else:
                    tapes[tape][heads[tape]] = line_split[4].strip('\n')
            elif direction == "HALT":
                print("Halted Execution")
                exit(1)
            else:
                print("Unrecognized Conditional!")
                exit(1)
    elif line_split[0] == "goto":
        line_number = int(line_split[1].strip('\n')) - 1
    elif line_split[0] == "write":
        tape = int(line_split[1])
        if(heads[tape] >= len(tapes[tape])):
            tapes[tape].append(line_split[2].strip('\n'))
        else:
            tapes[tape][heads[tape]] = line_split[2].strip('\n')
    elif line_split[0].strip('\n') == "print":
        print_tapes(tapes)
    elif line_split[0].strip('\n') == "halt":
        print("Halted Execution")
        exit(1)
    elif line_split[0] == "copytoend":
        tape = int(line_split[1].strip('\n'))
        tapes[tape].append(tapes[tape][heads[tape]])
    else:
        print("Unrecognized syntax on line {} \n {}".format(line_number, line))
        exit(1)
    line_number += 1

