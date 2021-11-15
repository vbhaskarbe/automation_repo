from collections import OrderedDict

items_count = int( input())
items_list  = OrderedDict()
for count in range(0, items_count):
    indata = input().split()
    price  = int(indata.pop())
    item   = ' '.join(str(i) for i in indata)
    if item not in items_list:
        items_list[item] = price
    else:
        items_list[item] = items_list[item] + price
    #print(item, items_list[item])
for item in items_list:
    print(item, items_list[item])


