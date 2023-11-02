

# 推导表达式逻辑 基本都是一样的，不一样的是 表达式最外侧的 括号：
#   []: 表示数组
#   {}: 表示集合或者字典，要根据 表达式的结构来做具体区分
#   (): 表示元祖


'''

列表推导式 其格式如下

[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]

或者 

[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
'''

def listDeriveExp():
    names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
    new_names = [name.upper() for name in names if len(name)>3]
    print(new_names) # ['ALICE', 'JERRY', 'WENDY', 'SMITH']

    # 计算30以内，被3整除的数
    args = [i for i in range(30) if i%3 == 0]
    print(args) # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

# listDeriveExp()

'''
字典推导式

{ key_expr: value_expr for value in collection }

或

{ key_expr: value_expr for value in collection if condition }

'''

def dictDeriveExp():
    listdemo = ['Google','Runoob','Taobao']
    newDict = {key: len(key) for key in listdemo}
    print(newDict) # {'Google': 6, 'Runoob': 6, 'Taobao': 6}

    # 以数字为key，幂次方为value
    numDict = {key: key**2 for key in range(1,7) if key%2==0}
    print(numDict) # {2: 4, 4: 16, 6: 36}

# dictDeriveExp()

'''
集合推导式
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }
'''
def setDeriveExp():
    list = [1,1,2,3,5,8,13]
    newSet = {ele for ele in list}
    print(newSet) # {1, 2, 3, 5, 8, 13}

    set1 = {x for x in 'abracadabra' if x not in 'abc'}
    print(set1) # {'r', 'd'}

# setDeriveExp()

'''
元祖推导式(生成器表达式)
(expression for item in Sequence )
或
(expression for item in Sequence if conditional )
'''
def setTupleExp():
    a = (x for x in range(1,6))
    print(a) ## <generator object setTupleExp.<locals>.<genexpr> at 0x10a441d20>

    print(tuple(a)) # (1, 2, 3, 4, 5)   使用 tuple() 函数，可以直接将生成器对象转换成元组

setTupleExp()

