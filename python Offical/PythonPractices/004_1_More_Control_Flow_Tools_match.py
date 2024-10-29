'''
albeit
     In fact, even functions without a return statement do return a value, albeit(尽管) a rather boring one.

ambiguity
    Methods of different types may have the same name without causing ambiguity(歧义). 
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):

    # print(f"cat point == x,y == {point.x}, {point.y} ")

    match point:
        case Point(x = 0, y = 0):
            print("origin")
        case Point(x = 0, y = y):
            print(f"x == 0 , y == {y}")
        case Point(x = x, y = 0):
            print(f"x == {x} , y == 0")
        case Point(x = x, y = y):
            print(f"location is x == {x}; y == {y}")
        case _:
            print("Not a point")

# p = Point(0,0)
# p = Point(0,10)
# p = Point(11,0)
# p = Point(11,22)
# p = Point(1,2)

p = (1,2)
where_is(p)

        