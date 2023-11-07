
## Many Values to Multiple variables

# python allows you to assgin values to multiple variables in one line
# Note: make sure the number of variables matches the number of values, or else you will get an error.
x, y, z = "ling","xiao","dai"
print(x,y,z)



## One value to Multiple variables

# you can assign the same value to multiple variables
x = y = z = "jackie dai"
print(x,y,z)


## Unpack a Colleciton

# If you have a colleciton of values in a list, tuple etc. Python allow you to extract the values into variables. This is called **unpacking**

fruits = ["apple","banana","peach"]
x, y , z = fruits
print(x,y,z)