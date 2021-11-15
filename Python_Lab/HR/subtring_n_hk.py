
string     = 'ABCDCDC'
sub_string = 'CDC'

count = 0
while string.find(sub_string) >= 0:
        count = count + 1
        index = string.find(sub_string)
        string = string[index+len(sub_string)-1:]
print(count)
