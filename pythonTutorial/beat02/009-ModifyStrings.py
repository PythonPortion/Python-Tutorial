## Upper Case

a = "Hello, Wrold"
print(a.upper())


## Lower Case

print(a.lower())

## Remove Whitespace
# whitespace is the space before and/or after the actual text, and very often you want to remove this space
b = "hj   kkkjkfff  ===     jkkl"

# Return a copy of the string with leading and trailing whitespace removed.

print(b.strip())

## Replace String

print(a.replace("H","J")) # Jello, Wrold


## Split String
# The split() method returns a list where the text between the specified separator becomes the list items
print(a.split(",")) # ['Hello', ' Wrold']