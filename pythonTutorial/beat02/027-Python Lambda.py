# Lambda（小写形式为λ，希腊字母）

# A lambda function is a small anonymous function.

x = lambda a: a + 10
print(x(10))


def myfunc(n):
    return lambda a : a * n

# doubleFunc = myfunc(2)
# print(doubleFunc(10))

print(myfunc(3)(4))