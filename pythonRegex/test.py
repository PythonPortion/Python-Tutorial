import re

# 横向匹配
def hor_match01():
    str = "abc abbc abbbc abbbbc abbbbbc abbbbbbc"

    pattern = r'ab{2,5}c'

    matchs = re.findall(pattern, str)
    if matchs:
        print('Match found:', matchs)
        # Match found: ['abbc', 'abbbc', 'abbbbc', 'abbbbbc']
    else:
        print('No match')

hor_match01()