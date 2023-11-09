thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical) # ['apple', 'banana', 'cherry', 'orange', 'mango', 'pineapple', 'papaya']

'''
(method) def extend(
    __iterable: Iterable[str],
    /
) -> None
'''

mytuple = (1,2,3)
tropical.extend(mytuple) ## ['mango', 'pineapple', 'papaya', 1, 2, 3]
