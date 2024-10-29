
def test01():
    tel = {'name': 'jackie', 'age': 18}
    print(tel)
    tel['height'] = 18
    print(tel)
    del tel['height']
    print(tel)
    del tel
    # print(tel) #这么做的话会出错


# test01()

def dict_test02():
    tel = dict(name='jackie', age=18, height=186)
    print(tel)

    tel1 = dict([('name', 'jackie'), ('age', 18), ('jj', 9.00)])
    print(tel1)

    return tel1


res = dict_test02()

for k, v in res.items():
    print(f"key : {k}, value : {v}")
