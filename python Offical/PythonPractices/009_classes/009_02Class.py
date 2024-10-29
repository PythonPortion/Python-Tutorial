class MyClass:

    '''A simple example class'''

    i = 123456

    def __init__(self):
        print("Init Func")

    def f(self):
        return "hello class"


def test01():
    x = MyClass()
    print(x.__doc__)

    print(x.i)

    print(x.f)

    print(x.f())

    print(x.__class__)

    print(MyClass.f(x))

    '''
    x.f() == MyClass.f(x)
    Python 中 实例对象的的实例方法会自动将改示例传递到方法体中
    '''


# test01()


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


def test2():
    x = Complex(3.0, -4.5)
    print(x.r, x.i)


# test2()

class Warehouse:
    purpose = 'storage'
    region = 'west'


def test3():
    x = Warehouse()
    print(x.purpose, x.region)

    x.region = 'southwest'
    print(x.purpose, x.region)


# test3()

def test4():

    dict = {1: "one", 2: "two", 3: "three"}

    for key in dict:
        print(key, dict[key])

    print("---------")

    for value in dict.values():
        print(value)

    print("++++++++++")

    for (key, value) in dict.items():
        print(key, value)

    print("==========")

# test4()