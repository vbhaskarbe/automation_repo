class MyDoc:
        "This is my second class"
        a = 10
        def func(self):
                print('Hello')

# Output: 10
print(MyDoc.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyDoc.func)

# Output: 'This is my second class'
print(MyDoc.__doc__)

mdoc = MyDoc()
mdoc.func()

