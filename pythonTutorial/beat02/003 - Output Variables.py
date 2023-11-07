## You can use the '+' operator to output multiple variables:
x,y,z = "Python ","is"," awesome"
print(x + y + z)

## For numbers, the + character works as a mathematical operator:
x, y = 5, 6
print(x + y) 

## In the print() function, when you try to combine a string and a number with the + operator , Python will raise an error
x, y = (5,"lingxiao")
print(x , y)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(x + y) 