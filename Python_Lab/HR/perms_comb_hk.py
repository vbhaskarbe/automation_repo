# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
textS, permk = input().split()
perm_list    = list(permutations( textS, int(permk)))
perm_list.sort()
[ print("".join(ch)) for ch in perm_list ]

'''
Task

You are given a string
.
Your task is to print all possible permutations of size

of the string in lexicographic sorted order.

Input Format

A single line containing the space separated string
and the integer value

.

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the permutations of the string

on separate lines.

Sample Input

HACK 2

Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''

