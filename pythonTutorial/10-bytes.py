x = bytes('hello',encoding="utf-8")
print(x) # b'hello'

y = x[1:3]
print(y) # b'el'

z = x + b"world"
print(z) # b'helloworld'

if x[0] == ord('h'):
    print("first ele is h")

print(ord('h')) ## 104