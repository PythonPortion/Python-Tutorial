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

'''
My first partnership was areadly being threatened with an eviction notice
'''