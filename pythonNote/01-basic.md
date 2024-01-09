[TOC]

# Variables

Variables are containers for stroring data values.

> **NOTE:**
>
> 1. Python has no command for declaring a variable
> 2. A variable is created when you first assgin a value to it
> 3. Variable can change type after they have been set.
> 4. Variable names are case-sensitive.

```python
x = 1
y = 2
print(x) # 1
print(y) # 2
y = "lx"
print(y) #lx
```

## Casting

> As the above describes, how to declare a variable expicity?
>
> - Via `Type-Casting` can do it. 

```python
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```

## Get the Type

> Similiar to lua, we can use the `type()` function to get a variable type.

```python
print(type(x)) # <class 'int'>
print(type(y)) # <class 'str'>
print(type(z)) # <class 'float'>
```

## Gloabl and Local Variable

> 1. Out of function's scope varibale is `Global`
>
> 2. Inside of function's scope varibale is `Local`
>
> 3. You can use the keyword `global` inside function to declare a gloabl variable
>
>    ```python
>    def myfunc():
>      global x
>      x = "fantastic"
>       
>    myfunc()
>       
>    print("Python is " + x) #Python is fantastic
>    ```
>  4. Using the `global` keyword can also change a global variable inside a function.

# DataTypes

Python has the following data types built-in by default, in these categories:

| Text Type:      | `str`                              |
| --------------- | ---------------------------------- |
| Numeric Types:  | `int`, `float`, `complex`          |
| Sequence Types: | `list`, `tuple`, `range`           |
| Mapping Type:   | `dict`                             |
| Set Types:      | `set`, `frozenset`                 |
| Boolean Type:   | `bool`                             |
| Binary Types:   | `bytes`, `bytearray`, `memoryview` |
| None Type:      | `NoneType`                         |

[更详细的类型请参考](https://www.w3schools.com/python/python_datatypes.asp)

## Strings

> - Strings in Python <u>**are arrays of bytes**</u> representing unicode characters.
> - <u>Python does not have a character data type</u>, a single character is simply a string with a length of `1`
> - Square brackets can be used to access elements of the string.

```python
a = "Hello, World!"
print(a[1]) # e
```

// TODO: @lingxiao string summary	https://www.w3schools.com/python/python_strings.asp

