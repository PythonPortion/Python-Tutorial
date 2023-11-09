thislist = ["apple", "banana", "cherry"]

for value in thislist:
    print(value)



print("==================")

## NOTE: Loop Through the Index Numbers

# You can also loop through the list items by referring to their index number.

# range = range(3)
range = range(len(thislist))

for value in range:
    print(thislist[value])


print("=========")

i = 0
while i < len(thislist):
    print(thislist[i])
    i = i+1


print("===list comprehension==")

[print(x) for x in thislist]
