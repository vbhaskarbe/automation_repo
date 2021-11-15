
x, k = ( int(x) for x in input().split())
polinomial = str(input())
print(x,k)
print(polinomial)
polinomial = polinomial.replace( 'x', str(x))
print(polinomial)
if eval(polinomial) == k:
    print(True)
else:
    print(False)

'''
Task

You are given a polynomial
of a single indeterminate (or variable), .
You are also given the values of and . Your task is to verify if

.

Constraints
All coefficients of polynomial
are integers.
and

are also integers.

Input Format

The first line contains the space separated values of
and .
The second line contains the polynomial

.

Output Format

Print True if

. Otherwise, print False.

Sample Input

1 4
x**3 + x**2 + x + 1

Sample Output

True

Explanation


Hence, the output is True.
'''

