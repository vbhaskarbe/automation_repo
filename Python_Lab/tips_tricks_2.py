
#11#Four Ways To Reverse String/List.
testList = [1, 3, 5]
testList.reverse()
print(testList)
#-> [5, 3, 1]

for element in reversed([1,3,5]): print(element)
#1-> 5
#2-> 3
#3-> 1

print("Test Python"[::-1])
print([1, 3, 5][::-1])

#12# Play With Enumeration.
testlist = [10, 20, 30]
for i, value in enumerate(testlist):
	print(i, ': ', value)
#1-> 0 : 10
#2-> 1 : 20
#3-> 2 : 30

#13# Use Of Enums In Python.
class Shapes:
	Circle, Square, Triangle, Quadrangle = range(4)

print(Shapes.Circle)
print(Shapes.Square)
print(Shapes.Triangle)
print(Shapes.Quadrangle)

#1-> 0
#2-> 1
#3-> 2
#4-> 3

#14# Return Multiple Values From Functions.
# function returning multiple values.
def x():
	return 1, 2, 3, 4
# Calling the above function.
a, b, c, d = x()
print(a, b, c, d)
#-> 1 2 3 4

#15# Unpack Function Arguments Using Splat Operator.
def test(x, y, z):
	print(x, y, z)
testDict = {'x': 1, 'y': 2, 'z': 3}
testList = [10, 20, 30]
test(*testDict)
test(**testDict)
test(*testList)
#1-> x y z
#2-> 1 2 3
#3-> 10 20 30

#16# Use A Dictionary To Store A Switch.
stdcalc = {
	'sum': lambda x, y: x + y,
	'subtract': lambda x, y: x - y
}
print(stdcalc['sum'](9,3))
print(stdcalc['subtract'](9,3))
#1-> 12
#2-> 6

#17# Calculate The Factorial Of Any Number In One Line.
import functools
FACT=5
result = (lambda k: functools.reduce(int.__mul__, range(1,k+1),1))(FACT)
print(result)
#-> 120

#18# Find The Most Frequent Value In A List.
test = [1,2,3,4,2,2,3,1,4,4,4]
print(max(set(test), key=test.count))
#-> 4

#19# Reset Recursion Limit.
#Python restricts recursion limit to 1000. We can though reset its value.
import sys
x=1001
print(sys.getrecursionlimit())
sys.setrecursionlimit(x)
print(sys.getrecursionlimit())
#1-> 1000
#2-> 1001

#20# Create A Dictionary From Two Related Sequences.
t1 = (1, 2, 3)
t2 = (10, 20, 30)
print(dict (zip(t1,t2)))
#-> {1: 10, 2: 20, 3: 30}

