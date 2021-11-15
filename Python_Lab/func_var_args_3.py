

def old_func(x, y, z, *args, **kwargs):
    print(x, y, z)
    print('positional args:', args)
    print('keyword args:', kwargs)
    if 'debug' in kwargs:
        print('do something new and exciting here')


old_func(1, 2, 3) # standard way to call this old function
old_func(1, 2, 3, 4, 5) # add some extra positional arguments
old_func(1, 2, 3, foo='bar', reverse=True) # add some keyword arguments
old_func(1, 2, 3, 4, 5, foo='bar', reverse=True) # add both
old_func(1, 2, 3, 4, 5, debug=True) # trigger debugging



