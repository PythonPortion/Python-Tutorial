


'''
String is Array in Python
'''

def stringIsArray():
    a = "hello"
    
    print(a[1]) # e

    for c in a:
        print("c == ", c)

# stringIsArray()
        
def string_len():
    a = "Hello, World!"
    print("a.len == ", len(a))

# string_len() # a.len ==  13

'''
Check String Using The Follow keywords:
    - "sub" in "parent"
        - if "sub" in "parent"
    - "sub" not in "parent"
        - if "sub" not in "parent"
'''

def check_string():
    a = "Hello, World!"
    print("Hello" in a) # True

# check_string()

def check_string_if_in():
    txt = "i love learn new things"
    if "love" in txt:
        print("contain the str")

# check_string_if_in()
        
'''
Slicing Strings 
NOTE:
    [a:b] == not contain b
    [-a: -b] == not contain -b
    [:b] == from left to b, not contain b
    [a:] == from left to end
'''
def slice_strings():
     a = "Hello, World!"
     # Get the characters from position 2 to position 5 (not included):
     b = a[:-5]
     print("type b == ", type(b)," b == ", b)

# slice_strings() ## type b ==  <class 'str'>  ...
     
'''
Modify Strings

'''
def modifyString():
    a = "abc123"
    b = a.upper()
    c = a.lower()
    print(b,c) # ABC123 abc123

    # remove whitespace :Whitespace is the space before and/or after the actual text
    d = "  hello world      "
    print("d len == ",len(d), "d ==:", d) # d len ==  19 d ==:   hello world 
    e = d.strip()
    print("e len == ",len(e), "e ==:", e) # e len ==  11 e ==: hello world

# modifyString()
    
def replace_Strings():
    a = "Hello Python"
    b = a.replace("H","*") # *ello Python
    print(b)

# replace_Strings()

def split_Strings():
    a = "a,bc,d"
    d = a.split(",")
    print("d.type ==:",type(d), "d ==:", d) #d.type ==: <class 'list'> d ==: ['a', 'bc', 'd']
# split_Strings()
    
'''
String Format
For More Pls See: https://www.w3schools.com/python/python_string_formatting.asp
'''
def string_format():
    a = 20
    b = "age is {}" 
    print(b.format(a)) # age is 20

    c, d, e = 5, 6, 7
    f = "ha ha {} bd {} ff {}"
    print(f.format(c,d,e)) # ha ha 5 bd 6 ff 7

    g = "_ha ha {2} bd {0} ff {1}"
    print(g.format(c,d,e))  # _ha ha 7 bd 5 ff 6

string_format()