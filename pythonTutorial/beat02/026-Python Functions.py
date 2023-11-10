## Arguments

## RECURSION

## Requirment: Caculate the sum between 1~100

def try_recursion(num):
    sum = 0
    if num > 0:
        sum = num + try_recursion(num-1)
        return sum
    else:
        return sum
    
print(try_recursion(100))