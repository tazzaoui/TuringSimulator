tape0 = *AlanTuring
print
move 0 END
move 0 RIGHT
write 0 $
move 0 END
movebackto 0 $
move 0 LEFT
if 0 * HALT
move 0 RIGHT
write 0 #
move 0 LEFT
copytoend 0
write 0 $
print
goto 5
