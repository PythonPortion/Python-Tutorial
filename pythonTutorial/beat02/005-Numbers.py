## There are three numeric types in Python: int,float,complex

# Varibales of numeric types are created when you assgin a value to them

x,y,z = 1, 3.14, 1j
print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'complex'>

x = -3j + 5j
y = 5
z = -5j

'''
'''

res = x + y + z
print(res) ## (5-3j)
print(type(res)) ## <class 'complex'>


print("---seperator line ---- Type Conversion ---- ")
## Type Conversion

x,y,z = 1, 3.14, 1j

a = float(x)
b = int(y)
c = complex(x)

print(type(a)," and ", a) # <class 'float'>  and  1.0
print(type(b)," and ", b) # <class 'int'>  and  3
print(type(c)," and ", c) # <class 'complex'>  and  (1+0j)

# NOTE: You cannot convert complex numbers into another number type

print("---seperator line ---- Random Number ---- ")

## Random Number

# Python does not have a random() function to make a random number, but Python has a built-in moudle called random that can be used to make random numbers:

import random

print(random.randrange(1, 10))
print(random.randrange(1, 10))
print(random.randrange(1, 10))
print(random.randrange(1, 10))



