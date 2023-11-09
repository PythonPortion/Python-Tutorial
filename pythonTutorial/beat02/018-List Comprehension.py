## NOTE: List Comprehension

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

## The Syntax

## NOTE: newlist = [`expression` for `item` in `iterable` if `condition == True`]

## NOTE 
# Condition is like a filter that only accepts the items that valuate to True, also, the condition can be omitted


print([x for x in range(10)])