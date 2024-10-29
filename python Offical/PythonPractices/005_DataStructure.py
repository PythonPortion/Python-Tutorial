def test1():
    stack = [3, 4, 5]
    item = stack.pop()
    print(item)


# test1()

def test2():
    squares = []
    for x in range(10):
        squares.append(x ** 2)
    print(squares)


# test2()


def test3():
    squares = list(map(lambda x: x ** 2, range(10)))
    print(squares)


# test3()

def test_4():
    squares = [x ** 2 for x in range(10)]
    print(squares)


# test_4()

def test_5():
    tt = [(x, y) for x in range(4) for y in range(4)]
    print(tt)


# test_5()

def test_6():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [10, 11, 12, 13]
    ]
    print(matrix)

    print("-----separate 11----")

    for row in matrix:
        print(row)

    '''
    上述 for loop 的 result 如下
        [1, 2, 3, 4]
        [5, 6, 7, 8]
        [10, 11, 12, 13]
    '''

    print("----")

    tmp = [row for row in matrix]
    print(tmp)
    # [[1, 2, 3, 4], [5, 6, 7, 8], [10, 11, 12, 13]]

    print("-----separate 22----")

    tmp = [[row[i] for row in matrix] for i in range(4)]
    print(tmp)
    # [[1, 5, 10], [2, 6, 11], [3, 7, 12], [4, 8, 13]]

    big_box = []
    for i in range(4):
        # i = 0,1,2,3
        sub_box = []
        # print(f"----loop index--{i}")
        for row in matrix:
            # print(row[i])
            sub_box.append(row[i])
        big_box.append(sub_box)

    print(f"big_box == {big_box}")

    tmp = list(zip(*matrix))
    print(f"----zip matrix == {tmp}")


# test_6()

def test_7():
    a = 'a'
    c = "a assci is %c" % a
    print(c)

    c2 = ord(a)
    print(c2)


test_7()