import json

x =  '{ "name":"John", "age":30, "city":"New York"}'

result = json.loads(x)
print(type(result))

print(result["name"])
print(result["age"])
print(result["city"])
# print(result.name)
# print(result.age)
# print(result.city)

'''
rise to dominance














import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
'''


x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)
print (y)

r = 0.041 / 12
b = 30 * 12
result = 1200000 * (r * pow(1 + r, b)) / (pow(1 + r, b) - 1)
print(result)

lixi = 1200000 * r
print(lixi)