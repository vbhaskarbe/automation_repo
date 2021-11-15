
from itertools import groupby

text_string = '1222311' #input()
comp_str = [(len(list(cgen)), int(ch)) for ch, cgen in groupby(text_string)]
for x in comp_str:
    print(x, end=" ")
print()

