from functools import reduce

# HARD - Maximize - incomplete

limit, percentile = ( int(x) for x in input().split())
#print( limit, percentile)
imax_list = []
temp_list = []
for count in range(0, limit):
    temp_list = [ int(x) for x in input().split() ]
    temp_list.pop(0)
    print(temp_list)
    temp_list.sort()
    imax_list.append(temp_list.pop())
smax_list = [ x*x for x in imax_list ]
smax = reduce( lambda x, y:x+y, smax_list)
print(smax % percentile)

