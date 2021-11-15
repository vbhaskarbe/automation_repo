
#List Comprehension
l = [i * i for i in range(1 ,10)]
print( l)

#Multiline strings
s = '''-:This is a string

that spans two lines.:-'''
print( s)

#Enumerate
movies = ('Interstellar', 'Predestination', 'Looper')
for i, movie in enumerate(movies):
    print((i, movie))

#Slicing
l = [3,4,5,6,7,8]
print( l[2:4] )
print( l[2:]  )
print( l[:4] )
print( l[::2])
print( l[::-1]  )
print( l[:5:2])
print( l[:4:2])

with open('./py_concepts.py', 'r') as file:
	for line in file:
		print(line)

