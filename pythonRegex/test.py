import re

pattern = r'.+'
# pattern = r'(\d+)([a-z]+)'

string = '123abc645'

match = re.match(pattern, string)
# if match:
#     print('Match found:', match.group())
# else:
#     print('No match')

if match:
    print('Full match:', match.group()) 
    # print('Full match:', match.group(0))   # 整个匹配到的字符串
    # print('First group:', match.group(1))  # 第一个组（\d+）
    # print('Second group:', match.group(2)) # 第二个组（[a-z]+）
    # print('Second group:', match.group(3)) # 第三个组（\d+）