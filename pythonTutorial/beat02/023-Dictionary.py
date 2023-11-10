car = {
    "id": 12,
    "username": "jackie",
    "gender": True
}

print(car.keys())
print(car.values())

listItems = car.items()
print(listItems)
print(type(listItems))


if "id" in car:
    print("exist")

for x in car.values():
    print(x)


for x,y in car.items():
    print(x," : ", y)

