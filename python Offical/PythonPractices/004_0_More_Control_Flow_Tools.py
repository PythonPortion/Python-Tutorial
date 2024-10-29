'''
excessive 
    The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive(过多) indentation. 

halt
    Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C), Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.

tricky
    Code that modifies a collection while iterating over that same collection can be tricky(棘手) to get right.

successive
    A match statement takes an expression and compares its value to successive patterns given as one or more case blocks. 

superficially
    This is superficially similar to a switch statement in C


    
'''

def test01():
    x = int(input("Pls enter an integer:\n"))
    if x < 0 :
        print("Negative Changed to zero")
    elif x == 0 :
        print("Zero")
    elif x == 1 :
        print("Single")
    else:
        print("More")

# test01()

'''
    - 
'''

def for_test01():
    words = ["cat","dog","window"]
    for item in words:
        print(item, len(item))
    
# for_test01()

def for_test02():
    users = {
        'Hans': 'active',
        'Eleonore': 'inactive',
    }

    # NOTE: 

    for user, status in users.copy().items():
    # for user, status in users.items():

        if status == 'inactive':
            del users[user]
            a = 10
    
    print("users == ",users)

# for_test02()


def range_01(args):
    # 可以通过range来生成数字
    for i in range(args):
        print(i)
        
# range_01(5)

def range_02():
    arr = list(range(5,10))
    print(arr) # [5, 6, 7, 8, 9]

    arr = list(range(1,10,2))
    print(arr) # [1, 3, 5, 7, 9]
# range_02()

def range_03():
    arr = ["Mary", "had", "a", "little", "lamb"]
    for i in range(len(arr)):
        item = arr[i]
        print(f"index == {i}, value == {item}")
    
    '''
        index == 0, value == Mary
        index == 1, value == had
        index == 2, value == a
        index == 3, value == little
        index == 4, value == lamb
    '''

    for i, v in enumerate(arr):
        print(f"---index == {i}, value == {v}")
    '''
        ---index == 0, value == Mary
        ---index == 1, value == had
        ---index == 2, value == a
        ---index == 3, value == little
        ---index == 4, value == lamb
    '''


# range_03()

def range_04():
    rg = range(0,10)
    print(rg)

# range_04()
        
def range_05():
    for num in range(2,10):
        if num % 2 == 0:
            print("--- even number == ",num)
            continue
        print("++++ even number == ",num)

    # while True:
    #     pass
    # print("12344----")
# range_05()  


def match_01(status):
    # 3.10 + 的版本才有 match 的语句，类似与其他语言的Switch
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 418:
            return "I'm a teapot"
        case 200 | 202 | 202 :
            return "all is succss"
        case _:
            return "Sth is wrong with the internet"
        
def testMatch():
    print(match_01(400))
    print(match_01(404))
    print(match_01(481))
    print(match_01(418))
    print(match_01(200))
    print(match_01(202))
    print(match_01(202))
        
# testMatch()

'''
    Patterns can look like unpacking assignment, and can be used to bind variables.
    这里有点类似于 Swift中 通过 switch 语句里 case 的解包操作
'''
def matchUnpack(args):
    match args:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y == {y}")
        case (x , 0):
            print(f"X == {x}")
        case (x, y):
            print(f"Location x == {x}; y == {y}")
        case _:
            raise ValueError("Not a point")

def testUnpack():
    tu = (1,2)
    print("---")
    print(type(tu))
    print("---")
    matchUnpack(tu)

# testUnpack()

# -------------------------------








