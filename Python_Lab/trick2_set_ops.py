a = [1, 2, 3, 'a']
b = ['a', 'b', 'c', 3, 4, 5]
print(set(a).intersection(b))

row = ["1", "bob", "developer", "python"]
print(','.join(str(x) for x in row))
print(*row, sep=',')

lines = []
lines.append("line1")
lines.append("line2")
lines.append("line3")
print("\n".join(lines))

a =  "codementor"
print("Reverse is",a[::-1])

mat = [[1, 2, 3], [4, 5, 6]]
zip(*mat)

list1 = ['a', 'b', 'c', 'd']
list2 = ['p', 'q', 'r', 's']
for x, y in zip(list1,list2):
    print(x, y)



