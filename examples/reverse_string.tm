tape = *AlanTuring
print
move END
move RIGHT
write $
move END
movebackto $
move LEFT
if * HALT
move RIGHT
write #
move LEFT
copytoend
write $
print
goto 5