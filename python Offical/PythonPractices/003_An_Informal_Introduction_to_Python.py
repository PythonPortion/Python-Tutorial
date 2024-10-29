'''
presence
absence
    In the following examples, input and output are distinguished by the presence or absence of prompts

clarify
    Since comments are to clarify code and are not interpreted by Python

straightforward
    Expression syntax is straightforward

fractional
    a fractional part 

masking
    Don’t explicitly assign a value to it — you would create an independent local variable with the same name masking the built-in variable with its magic behavior.

preface
    If you don’t want characters prefaced by \ to be interpreted as special characters

subtle
    There is one subtle aspect to raw strings

workaround
    for more information and workarounds.

span
    String literals can span multiple lines

glued
    Strings can be concatenated (glued together) with the + operator, and repeated with *:

corresponding
    the second row gives the corresponding negative indices.

gracefully
    However, out of range slice indexes are handled gracefully when used for slicing:

compound
    Python knows a number of compound data types, used to group together other values

versatile
    The most versatile is the list

comparison
    The test used in the example is a simple comparison. 

decent
facility
    all decent text editors have an auto-indent facility

'''

print("----111-----")
print("""
Usage: thingy [OPTIONS]
    -h
    -H hostname
""")
print("----2222-----")
print("""\
Usage: thingy [OPTIONS]
    -h
    -H hostname
""")
print("----3333-----")

# Find the distinguishs on above.

a, b = 0, 1
while a < 10:
    # a = b
    # b = a + b
    # print(a)  # 1  2   4   8  16
    print(a)
    a, b = b , a+ b
    