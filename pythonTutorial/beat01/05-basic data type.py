'''
Python 中的变量，不需要声明。每个变量在使用前都必须赋值，变量赋值以后才会被创建

Python 中，变量就是变量，没有类型。 我们所说的“类型”是指 变量所指的内存中对象的类型
'''

'''

counter = 100
miles = 1000.0
name = "jackie"

print(counter)
print(miles)
print(name)

'''


# 多变量赋值
'''
a = b = c = 1
print(a,b,c)

e,f,g = 4,5,"jackie"
print(e,f,g)



a,b,c,d = 20,5.5,True,4+3j
print(type(a),type(b),type(c),type(d))
# 输出结果：<class 'int'> <class 'float'> <class 'bool'> <class 'complex'>

# 还可以用 isinstance 来判断
print(isinstance(a, int)) # True

# type() 不会认为 子类是一种 父类类型
# isinstance() 会认为 子类 是一种 父类类型


'''

# bool (布尔类型)

'''
a = True
b = False

print(2 < 3)
print(2 == 3)

print(a and b)
print(a or b)
print(not a)

print(int(a))
print(float(b))
print(str(a))
'''