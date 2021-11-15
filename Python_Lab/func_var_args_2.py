# If you use **kwargs in your function header, your function can accept an arbitrary number of keyword arguments, i.e., key-value pairs:

def func(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])

func(x=1, foo='bar', reverse=True)


