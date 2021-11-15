n, m = [ int(x) for x in input().split() ]
iarray = [ x for x in input().split() ]
s1  = set(input().split())
s2  = set(input().split())

total_happiness = 0
for x in iarray:
    #print(x)
    if x in s1:
        total_happiness = total_happiness + 1
    if x in s2:
        total_happiness = total_happiness - 1

print(total_happiness)


#print(n,m)
#print(iarray)
#print(s1)
#print(s2)

'''
Constraints


Input Format

The first line contains integers
and separated by a space.
The second line contains integers, the elements of the array.
The third and fourth lines contain integers, and

, respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7

Sample Output

1

'''
