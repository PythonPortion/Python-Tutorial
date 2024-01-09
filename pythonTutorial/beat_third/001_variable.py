x = 1
y = 2
print(x) # 1
print(y) # 2
y = "lx"
print(y) #lx

z = float(3)
print(type(x)) # <class 'int'>
print(type(y)) # <class 'str'>
print(type(z)) # <class 'float'>


def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)



a = "Hello, World!"
print(a[1])