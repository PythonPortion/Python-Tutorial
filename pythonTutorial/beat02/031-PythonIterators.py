## Iterator VS Iterable

# > Lists,tuples,dictionaries ,sets are all iterable objects. They are iterable containers which you can get an iterator from.

myTuple = ("ling","xiao","dai")
myit = iter(myTuple)

print(next(myit))
print(next(myit))
print(next(myit))
# print(next(myit))
'''
chef ,厨师， chef 厨师
'''