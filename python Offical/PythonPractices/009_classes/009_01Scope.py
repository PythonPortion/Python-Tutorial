import builtins

# a = abs(-5)
# print(a)

# print(builtins)

a = "global var"


def test_scope():
    # print(a) ## 输出 "global var"

    global a
    a = "enclose global var"
    print(a)

    # a = b
    a = "enclose global var 2"


test_scope()

print(a)