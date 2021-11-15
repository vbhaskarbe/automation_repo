
#*args is Python syntax which allows you to create a function which takes a variable number of arguments:
def product(*args):
    prod = 1
    for term in args:
        prod *= term
    return prod

print( product(1, 2, 3, 4, 5, 6, 7, 8, 9))

