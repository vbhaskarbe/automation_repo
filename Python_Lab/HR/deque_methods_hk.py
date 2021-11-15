
from collections import deque

d_actions_max = 6
d_actions_list = [ [ 'append', 1],
                  [ 'append', 2],
                  [ 'append', 3],
                  [ 'appendleft', 4],
                  [ 'pop' ],
                  [ 'popleft' ] ]
action, param = str(input()).split()

d_actions_list.append([ action, param ])
print(d_actions_list)
#print(d_actions_max)
#print(d_actions_set)
d = deque()
'''
d.append(1)
d.append(2)
d.append(3)
d.appendleft(4)
print(d)
print(d.pop())
print(d.popleft())
print(d)

'''
for d_action in d_actions_list:
    d_action_name  = d_action[0]
    #print(d_action_name)
    if len(d_action) > 1:
        d_action_param = d_action[1]
        #print(d_action_param)
        d_method = getattr(d, d_action_name)
        d_method(d_action_param)
    else:
        d_action_param = ''
        getattr(d, d_action_name)()
print(' '.join(str(x) for x in d))
