# NOTE: The Type of tuple is very similar to list. most api can be used in tuple

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) ## ['cherry', 'strawberry', 'raspberry']


(green, *yellow, red) = fruits

print(green)
print(yellow) ## ['banana', 'cherry', 'strawberry']
print(red)
