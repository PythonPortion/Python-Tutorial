def test1():
    s = 'hello'
    it = iter(s)
    print(it)

    print(next(it))
    print(it.__next__())

    print(next(it))
    print(it.__next__())

    print(next(it))
    # print(it.__next__())


# test1()

def test2():
    class Reverse:
        def __init__(self, data):
            self.data = data
            self.__index = len(data)

        def __iter__(self):
            return self

        def __next__(self):
            if self.__index == 0:
                raise StopIteration

            self.__index = self.__index - 1
            return self.data[self.__index]

    rev = Reverse("Hello")
    for item in rev:
        print(item)


# test2()


def test3():
    def reverse(data):
        # for index in range(len(data) - 1, -1, -1):

        print("---len == ",len(data))

        for index in range(len(data) - 1, -1, -1):
            print(index)
            yield data[index]

    for char in reverse('golf'):
        print(char)


test3()