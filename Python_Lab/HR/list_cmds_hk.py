
if __name__ == '__main__':
    N = int(input())
    #cmd_count = int( input())
    t_list    = list()
    while N > 0 :
        cmd_params = input().split()
        cmd        = cmd_params[0]
        *params,   = ( int(x) for x in cmd_params[1:])
        if cmd == 'print':
            print(t_list)
        else:
            my_cmd = getattr(t_list, cmd)
            my_cmd(*params)
        N = N - 1


'''
Input Format

The first line contains an integer,
, denoting the number of commands.
Each line of the

subsequent lines contains one of the commands described above.

Constraints

    The elements added to the list must be integers.

Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]


'''
