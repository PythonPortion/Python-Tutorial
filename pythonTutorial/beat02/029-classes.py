## Python Classes and Objects

### Python Classes/Objects

# Python is an Object oriented programming language.

# Almost everything in Python is an object, with is properties and methods.

# A class is like an constructor, or a 'blueprint' for creating objects.


## Create a Class
# > To create a class, use the keyword `class`:

class MyClass:
    x = 9

## Create Object
# > Now we can use the class method named MyClass to create objects:

p1 = MyClass()
print(p1.x)


## The __init__() Function

# > the examples above are classes and objects in their simplest form, and are not really useful in real life applications.

# > To understand the meaning of classes we have to understand the built-in __init__() function.

# > All Classes has a function called __init__(),which is always excuted when the class is being intiated.

# > Use the __init__() function to assgin values to object properties, or other operations that are necessary to do when the objects is being created:

class Person:
    # NOTE: the __init__() function is called automatically every time the class is being used to create a new object.
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("jackie",18)
print(p1)
print("name == ",p1.name)
print("age == ",p1.age)

print("----------------------------")

## The __str__() function

# > the __str__() function controls what should be returned when the object is represented as a string.

# > If the __str__() function is not set, the string representation of the object is returned as follows:

print(p1) ## <__main__.Person object at 0x10b2a2da0>

# > The string representation of an object with the __str__() function,

# > Personal Comprehension: the function named __str__() is similar to description() in Swift

class MalePerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f"{self.name}({self.age})"
    
male = MalePerson("Hero","199")
print(male) # Hero(199) 

print("---------------------")

## Object Methods

# Objects can also contain methods. Methods in objects are funcitons that belong to the object.

## NOTE: the 'self' here is the same as in swift

class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def myFunc(self):
        print(f"Hello my name is {self.name},age is {self.age}")

a = Animal("donkey",3)
a.myFunc()