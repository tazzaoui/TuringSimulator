# TuringSimulator
A small language for simulating the behavior of Turing Machines

## The Language
1. Every file must start with a definition of the initial contents of the tape e.g. ```tape = 123456```
2. Reserved keywords for interacting with the read/write head & the tape are as follows

| Operation | Description |
| --- | --- |
| move {LEFT \| RIGHT \| END \| START}| Move the head one block of tape to the left/right or to either end of the tape|
| moveto x | Move to the first block of tape on the right that has the char 'x' written on it. Stay in place if no such block exists|
| movebackto x | Move to the first block of tape on the left that has the char 'x' written on it. Stay in place if no such block exists|
| if x {LEFT \| RIGHT\| HALT} | If the block under the head reads the char 'x', move left/right or halt|
| if a WRITE b| If the block under the head reads the char 'a', replace it with the char 'b'|
| ifnot x {LEFT \| RIGHT\| HALT} | If the block under the head does not read the char 'x', move left/right or halt|
| ifnot a WRITE b| If the block under the head does not read the char 'a', replace it with the char 'b'|
| goto n | Jump to line n (zero-indexed) and continue executing from there|
| write x | Replace the char on the block under the head with 'x'|
| print | Print the contents of the tape |
| copytoend | Append the char on the block under the head to the end of the tape |

See examples in the ```examples``` directory for more

## To Use
Write your logic in a file, and invoke ```turing_parser.py``` with the path to that file as an argument. 

e.g. ```python3 turing_parser.py examples/add.tm```
