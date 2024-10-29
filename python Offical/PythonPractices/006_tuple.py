t = '1', 2, 3.14, 'hello world', "I Love China"
print(t)

print(type(t))

print(t[3])

# t[3] = "JJJ" # tuple not support assignment

t2 = ([1, 2, 3], [7, 8, 9])
print(t2)
t2[1].append(5)
print(t2)

x, y, z = "dai", "ling", "xiao"
print(f"x == {x}, y == {y}, z == {z}")


a = set("abracadabra")
print(a)
a = {"abracadabra"}
print(a)