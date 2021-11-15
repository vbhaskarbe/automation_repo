# function to print the first m multiple
# of a number n without using loop.
def multiple(m, n):
 
    # inserts all elements from n to 
    # (m * n)+1 incremented by n.
    a = range(n, (m * n)+1, n)
    print(a)     
    print(*a)
 
# driver code 
m = 10
n = 3
multiple(m, n)

#In Python 3, print(*(range(x)) is equivalent to print(" ".join([str(i) for i in range(x)]))




