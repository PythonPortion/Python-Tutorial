'''
元祖的元素不能修改

string , list , tuple 都属于 Sequence(序列)

'''

tuple = ('a','b',1,2,3.1415926)
tinyTuple = (123, 'jackie')

print(tuple)                # ('a', 'b', 1, 2, 3.1415926)
print(tuple[0])             # a
print(tuple[1:3])           # ('b', 1)
print(tuple[2:])            # (1, 2, 3.1415926)
print(tinyTuple*2)          # (123, 'jackie', 123, 'jackie')
print(tinyTuple + tuple)    # (123, 'jackie', 'a', 'b', 1, 2, 3.1415926)



'''
python 中 字符串 跟 元祖比较类似，可以 把 字符串看成 特殊的元祖
'''