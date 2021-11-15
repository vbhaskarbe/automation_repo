import sys
print("Current Python version: ", sys.version)

#1# In-Place Swapping Of Two Numbers.
x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)
#1 (10, 20)
#2 (20, 10)

#2# Chaining Of Comparison Operators.
n = 10
result = 1 < n < 20
print(result)
# True
result = 1 > n <= 9
print(result)
# False

#3# Use Of Ternary Operator For Conditional Assignment.
#[on_true] if [expression] else [on_false]
x = 10 if (y == 9) else 20
print(x)
#x = (classA if y == 1 else classB)(param1, param2)
def small(a, b, c):
	return a if a <= b and a <= c else (b if b <= a and b <= c else c)

print(small(1, 0, 1))
print(small(1, 2, 2))
print(small(2, 2, 3))
print(small(5, 4, 3))

print([m**2 if m > 10 else m**4 for m in range(50)])
#Output
#0 #1 #2 #3

multiStr= ("select * from multi_row "
"where row_id < 5 "
"order by age")
print(multiStr)

#select * from multi_row where row_id < 5 order by age

#4#Storing Elements Of A List Into New Variables.
testList = [1,2,3]
x, y, z = testList
print(x, y, z)
#-> 1 2 3

#5# Print The File Path Of Imported Modules.
import threading 
import socket
print(threading)
print(socket)
#<module 'threading' from '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/threading.py'>
#<module 'socket' from '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/socket.py'>

#6#Dictionary/Set Comprehensions.
testDict = {i: i * i for i in range(10)}
testSet = {i * 2 for i in range(10)}
print(testSet)
print(testDict)
#set([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#7# Debugging Scripts.
import pdb
#pdb.set_trace()
#We can specify <pdb.set_trace()> anywhere in the script and set a breakpoint there. It’s extremely convenient.

#8# Setup filesharing.
## at CLI: python3 -m http.server
#Above commands would start a server on the default port i.e. 8000. You can also use a custom port by passing it as the last argument to the above commands.

#9# Inspect an object in python
test = [1, 3, 5, 7]
print( dir(test) )

#10#Combining multiple strings
test = ['I', 'Like', 'Python', 'automation']
print(''.join(test))

