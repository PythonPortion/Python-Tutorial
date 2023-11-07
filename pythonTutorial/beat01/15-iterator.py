# 迭代器有两个基本的方法：iter() 和 next()。

import sys

list = [1,2,3,4]
it = iter(list)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for x in it:
    print(x, end=" ")

# StopIteration 表示迭代完成的标记
'''
while True:
    try:
        print(next(it))
    except StopIteration: 
        sys.exit()
'''


'''
如果一个类要作为迭代器使用，则必须实现两个方法
__iter__()
__next__()
'''

class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myClass = Mynumbers()

myiter = iter(myClass)
 
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print('============分割线=============')

'''
yield 定义生成器函数，是一种特殊的函数，在迭代过程中逐步产生值，而不是一次性返回所有的值

当生成器函数中使用yield 语句时，函数的执行将会暂停，并将yield 后面的表达式座位当前迭代的值返回, 下一次调用 会从上次 暂停的地方继续执行，直到再次遇到yield语句。


生成器函数的优势是它们可以按需生成值，避免一次性生成大量数据并占用大量内存。

简单理解: 迭代器就是一个生成器
'''

def countdown(n):
    while n>0:
        yield n
        n -= 1

# create generator instance
generator = countdown(5)

# retrieve values by calling an iterator-generator
print(next(generator)) # 5
print(next(generator)) # 4
print(next(generator)) # 3

# use for loop to trigger generator
for value in generator:
    print(value, end=" ") 


print("==separator line===")

# 生成一个fibonacci 数列

def fibonacciSequence(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

count = 10
f = fibonacciSequence(count)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

for v in f:
    print(v, end=" ")