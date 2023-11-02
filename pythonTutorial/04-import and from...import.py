# 导入 sys 模块
'''
import sys

print("==========Python import mode=====")

print('命令行参数为')

for i in sys.argv:
    print(i)

print("\n python path is", sys.path)
'''

print('================python from import===================================')
# 导入特定的成员
from sys import argv, path

for i in argv:
    print(i)

print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

