if 'a' in {'a','b'}:
    print("contain character a")


    
i = 5

def args(arg = i):
    print(f"arg == {arg}")

i = 100

args() ## arg == 5

print("--------------------")


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))

print(f(2))


print(f(3))