D1 = { 'Name': 'Geeks', 1: [1, 2, 3, 4]} 
D2 = {1: 'Geeks', 2: 'For', '3': {'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}} 
for x in D2:
    print(x)
print("***************\n")
for x in D1:
    print(D1[x])
print("======   Final   ======")
D1 = { 'Name': 'Geeks', 1: [1, 2, 3, 4]} 
for x,y in D1.items():
    print(x, y)
