
list = [
    "abcd",
    123,89.9,
    'jacke',
    False
    ]

tinylist = [456,'memo']

print(list)         # ['abcd', 123, 89.9, 'jacke', False]

print(list[0])      # abcd

print(list[1:3])    # [123, 89.9]; 取值范围 index == 1  ~ index == [3-1]

print(list[2:])     # [89.9, 'jacke', False]

print(tinylist * 2) # [456, 'memo', 456, 'memo']

print(list + tinylist) # ['abcd', 123, 89.9, 'jacke', False, 456, 'memo']


wholeList = [0,1,2,3,4,5,6,7,8,9]
print(wholeList[2:8:2]) # [2, 4, 6]

'''
[-1::-1]
# 第一个参数 -1 表示最后一个元素
# 第二个参数为空，表示移动到列表末尾
# 第三个参数为步长，-1 表示逆向
'''
print(wholeList[-1::-1])

def reverseWords(input):
    inputWords = input.split(" ")

    inputWords = inputWords[-1::-1]

    inputWords = " ".join(inputWords)

    return inputWords

result = reverseWords("YOU LOVE I")

print("result == ",result)

print("list length == ",len(wholeList))