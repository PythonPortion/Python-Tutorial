## Strings

# Strings in python are surrounded by either single quotation marks, or double quotation marks


## Strings are Arrays

# Like many other programing languages, strings in Python are arrays of bytes respenting unicode characters.

# NOTE: There is no character data type in Python.

a = "hello, world"
print(a[1])

print("------Separator --- line -------")

## Looping Through a String

# Since Strings are array, we can loop through the characters in a string ,with a for loop

for x in "banana":
    print(x)

print("------Separator --- line -------")

## String length
print(len(a))


print("------Separator --- line -------")
## Check String

# To check if a certain phrase or character is present in a string, we can use the keyword *in*
txt = "The best things in lift are free"
print("free" in txt)

print("freeddd" not in txt)