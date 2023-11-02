'''
Python 中的字典 跟 Swift 和 OC 类似
'''

dict = {}
dict["one"] = 1
dict[2] = "2-test"

# print(dict) # {'one': 1, 2: '2-test'}

'''
字典推导式，这个后面介绍
'''
dict1 = {x: x**2 for x in (2,3,6)}
print(dict1) # {2: 4, 3: 9, 6: 36}