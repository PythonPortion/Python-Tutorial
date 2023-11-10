## NOTE: A set is a collection which is unordered, unchangeable and unindexed.

mySet = {"chat","gpt","grand"}

'''
for value in mySet:
    print(value)
'''

print('meset address == ', mySet)

# NOTE: Once a set is created, you cannot change its values, but you can add new items??? why?

mySet.add('very')

for value in mySet:
    print(value)

print('meset address == ', mySet)

print("----------")


anotherSet = {"a",1,2}

# print(anotherSet)

mySet.update(anotherSet)
print(mySet)

print("-----------")


set1 = {1,2,3}
set2 = {"a","b","c"}

set3 = set1.union(set2)
print(set3)

set4 = {'x','y','z'}
set4.update(set1)
print(set4)

print("-----------")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

print("-----------")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)


print('------')

