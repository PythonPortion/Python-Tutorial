## Global Variables

# The Definition is that variables created outside of functions

# Note: If you create a variable with the same name inside a funciton, this varibale will be local, and can only be used inside the funciton, The gloabl variable with the same will retain as it was, gloab and with the original value

x = "awesome"

def myFunc():
    x = "fantastic"
    print("inside the function x == ",x)
    # inside the function x ==  fantastic

myFunc()
print("global variable x == ", x)
# global variable x ==  awesome


## The global keyword

# Normally, when you create a variable inside a function,that variable is local, and can only be used in that function.

# To create a gloabl variable inside a funciton, you can use the `global` keyword

# myFunc(True)
# print("global variable x == ", x)


def myFunc1():
    global x
    x = "fantastic"
    print("inside the function x == ",x)
    # inside the function x ==  fantastic

myFunc1()
print("global variable x == ", x)
# global variable x ==  fantastic