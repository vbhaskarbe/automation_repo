## Merge 2 Dictionaries - avoid duplicates in Python 3.5+

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(x)
print(y)
print("Merged dict is : ", z)


