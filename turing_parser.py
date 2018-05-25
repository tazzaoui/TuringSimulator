#!/usr/bin/env python3

import sys

def print_tape(tape):
    for i in tape:
        sys.stdout.write("[{}]".format(i))
    print('')

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    exit(1)

input_file = list()
tape = list()
line_number = 1
head = 0

with open(sys.argv[1], 'r') as f:
    input_file = f.readlines()

print("Reading {}...".format(sys.argv[1]))
print("Read in {} instructions...\n".format(len(input_file)))

t = input_file[0].split(' ')[2]
for i in range(len(t) - 1):
    tape.append(t[i])


while input_file[line_number] != "done":
    line = input_file[line_number]
    line_split = line.split(" ")
    if line_split[0] == "move":
        direction = line_split[1].split("\n")[0]
        if direction == "RIGHT":
            head += 1
        elif direction == "LEFT":
            if(head > 0):
                head -= 1
        elif direction == "END":
            head = len(tape) - 1
        elif direction == "START":
            head = 0
        else:
            print("ERROR ON LINE {}. No such direction: {}".format(line_number,direction))
            exit(1)
    elif line_split[0] == "moveto":
        target = line_split[1].strip('\n')
        for i in range(head, len(tape)):
            if(tape[i] == target):
                head = i
                break
    elif line_split[0] == "movebackto":
        target = line_split[1].strip('\n')
        i = len(tape) - 1
        while(i >= 0):
            if(tape[i] == target):
                head = i
                break
            i -= 1
    elif line_split[0] == "if":
        if(tape[head] == line_split[1].strip('\n')):
            direction = line_split[2].strip('\n')
            if direction == "RIGHT":
                head += 1
            elif direction == "LEFT":
                if(head > 0):
                    head -= 1
            elif direction == "WRITE":
                if(head >= len(tape)):
                    tape.append(line_split[3].strip('\n'))
                else:
                    tape[head] = line_split[3].strip('\n')
            elif direction == "HALT":
                print("Halted Execution")
                exit(1)
            else:
                print("Unrecognized Conditional!")
                exit(1)
    elif line_split[0] == "ifnot":
        if(tape[head] != line_split[1].strip('\n')):
            direction = line_split[2].strip('\n')
            if direction == "RIGHT":
                head += 1
            elif direction == "LEFT":
                if(head > 0):
                    head -= 1
            elif direction == "WRITE":
                if(head >= len(tape)):
                    tape.append(line_split[3].strip('\n'))
                else:
                    tape[head] = line_split[3].strip('\n')
            elif direction == "HALT":
                print("Halted Execution")
                exit(1)
    elif line_split[0] == "goto":
        line_number = int(line_split[1].strip('\n')) - 1
    elif line_split[0] == "write":
        if(head >= len(tape)):
            tape.append(line_split[1].strip('\n'))
        else:
            tape[head] = line_split[1].strip('\n')
    elif line_split[0].strip('\n') == "print":
        print_tape(tape)
    elif line_split[0].strip('\n') == "halt":
        print("Halted Execution")
        exit(1)
    elif line_split[0].strip('\n') == "copytoend":
        tape.append(tape[head])
    else:
        print("Unrecognized syntax on line {} \n {}".format(line_number, line))
        exit(1)
    line_number += 1

