# 不定参数，以* 开头，表示 tuple

def testMultiArgs(arg, *args):
    print(arg, type(arg))
    print(args, type(args))

# testMultiArgs(10,20,40,50)
'''
10 <class 'int'>
(20, 40, 50) <class 'tuple'>
'''

# 不定参数，以** 开头，表示 dict
def testMuiltDic(arg, **args):
    print(arg, type(arg))
    print(args, type(args))

testMuiltDic('124', a = 2, b = 3, c = "123")
'''
124 <class 'str'>
{'a': 2, 'b': 3, 'c': '123'} <class 'dict'>
'''

'''
lambda 函数的语法只包含一个语句，如下：
lambda [arg1 [,arg2,.....argn]]:expression
'''

x = lambda a: a + 10
print(x(10)) # 20

sum = lambda a, b: a + b
print(sum(4, 5))


4 + 3