## Slicing

# You can return a range of characters by using the slice syntax

b = "Hello, LiHuanYing"
print(b[2:5]) # llo,


## Slicing from the start

# by leaving out the start index, the range will start at the first character
print(b[:5]) # Hello

print(b[2:]) # llo, LiHuanYing


## Negative Indexing
# Use negative indexes to start the slice from the end of the string

print(b[-5:-1]) # nYin