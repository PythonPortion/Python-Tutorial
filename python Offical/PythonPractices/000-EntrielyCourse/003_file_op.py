def tt1():
    f = open('foo.txt', 'rt')
    data = f.read()
    print(data)

    g = open('bar.txt', 'wt')
    g.write('some text')

    f.close() # it's easy to forget this statement
    g.close() # it's easy to forget this statement


# tt1()

# As it's easy to forget 'close' statement. so there is another approach to instead of that.

def tt2():
    with open('foo.txt', 'rt') as f:
        data = f.read()
        print(data)

    with open('bar.txt', 'wt') as f:
        print('Hello World', file=f)
        # f.write("hello kitty -- 99")

        print("-----write func----")

    # with open("bar.txt", 'rt') as f:
    #     data = f.read()
    #     print(data)


tt2()


