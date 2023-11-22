import datetime

# For more details, pls refer to link: https://www.w3schools.com/python/python_datetime.asp

x = datetime.datetime.now()
print(x) # 2023-11-20 13:26:21.946853

print(x.year) # 2023

print(x.strftime('%A')) # Monday
print(x.strftime('%a')) # Mon


x = datetime.datetime(2023,11,20)
print(x) # 2023-11-20 00:00:00
print(x.strftime('%B')) # November
print(x.strftime('%b')) # Nov
