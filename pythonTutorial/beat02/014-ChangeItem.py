## Change a range of item values

# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# If you insert more items than you replace, the new items will inserted where you specified, and the remaining items will move accordingly
thislist[1:3] = ["blackcurrant", "watermelon", "watermelon1"]
print(thislist)

thislist[1:] = ["blackcurrant"]
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


## Insert Items
myList = ["apple", "banana", "cherry"]


# insert obj before index == 1
myList.insert(1, "watermelon")
print(myList)