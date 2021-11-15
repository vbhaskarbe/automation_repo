n = 10
result = 1 < n < 20
print(result)
result = 1 > n <= 9
print(result)

#Library path
import os;
import socket;
 
print(os)
print(socket)

#Enums
class MyName:
    Geeks, For, Geeks = range(3)

print(MyName.Geeks)
print(MyName.For)
print(MyName.Geeks)

#Return multiple
def x():
    return 1, 2, 3, 4
a, b, c, d = x()

print(a, b, c, d)

#Most frequent value in a list
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key = test.count))





