

def test():
    sites = {'Google','Taobao','Zhihu','Baidu','Taobao'}

    print(sites) # {'Google', 'Taobao', 'Baidu', 'Zhihu'} ；重复的元素‘Taobao’ 自动去除了

    if 'Taobao' in sites:
        print("exit element")
    else:
        print("no exit")    

# test()

def setOp():
    a = set({"1","2","3","4","5"})
    b = set({"3","4","5","6"})
    print(a)
    print(b) 

    # 差集
    # a-b: 表示 所有 a 中，不包含 b 的元素  的 集合
    print(a-b) # {"1", "2"}
    # b-a: 表示 所有 b 中，不包含 a 的元素  的 集合
    print(b-a) # {"6"}

    # 并集 ： 将两个或多个集合的所有元素合并到一起，形成一个包含所有元素的新集合
    print(a|b) # {'2', '4', '6', '1', '3', '5'}
    print(b|a) # {'4', '1', '3', '6', '2', '5'}

    # 交集 :
    print(a&b) # {'5', '4', '3'}

    # a 和 b 中不同时存在的元素
    print(a^b) # {'1', '2', '6'}

    print((a|b)-(a&b)) # {'6', '2', '1'}

setOp()

