from timeit import Timer

def hello():
    print("hello, world")

t = Timer(5.0, hello())
t.start()  # after 30 seconds, "hello, world" will be printed


