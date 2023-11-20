
## Python Inhertiance

# > Inhertiance allow us to define a class that inherits all the methods and properties from another class.

# > Parent Class is the class being inherited from, also called base class.

# > Child Class is the class that inherit from another class, also called derived class


######## Create a parent class

class Person:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname
    
    def printName(self):
        print(self.fname, self.lname)
    
p = Person('lingxiao','Dai')
p.printName()

print("-------------------------------")
####### Create a Child class

# NOTE: To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

class Student(Person):
    pass

p = Student('lingxiao1','Dai')
p.printName()



######### Add the __init__() function
# > So far we had created a child class that inherits the properties and methods from its parent class

# > We want to add the __init__() function to the child class

class Teacher(Person):
    def __init__(self, fname, lname, experience) -> None:
        super().__init__(fname, lname)
        self.experience = experience
    
  
    
t = Teacher('daofu','wang',20)
t.printName()