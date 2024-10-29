'''
guru  （专家）  
    check with your local Python guru or system administrator.

beep

analogous
    A second way of starting the interpreter is python -c command [arg] ..., which executes the statement(s) in command, analogous to the shell’s -c option.

thereafter
turn into
    When known to the interpreter, the script name and additional arguments thereafter are turned into a list of strings and assigned to the argv variable in the sys module.

convention
portable
    a convention that any portable code should follow

'''

'''
control + D === exit python interpreter
control + p === get the previous cmd you inputed
'''

'''
test argument passing
'''

import sys
print(f"argv[0] == {sys.argv[0]}")
print(f"argv[1] == {sys.argv[1]}")