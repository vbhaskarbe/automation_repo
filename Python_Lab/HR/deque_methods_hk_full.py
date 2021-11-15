# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

if __name__ == '__main__':
    dq = deque()
    ## Get total actions
    dq_actions_count = int( input())
    dq_actions_list  = []
    ## Read DQ actions and store in list
    while dq_actions_count > 0:
        dqaction  = str(input()).split()
        #print( dqaction)
        if len(dqaction) > 1 :
            dq_actions_list.append( [ dqaction[0], dqaction[1]])
        else:
            dq_actions_list.append( [ dqaction[0]])
        dq_actions_count = dq_actions_count - 1

    print(dq_actions_list)
    
    ## Process actions and perform
    for dq_action in dq_actions_list:
        dq_action_name  = dq_action[0]
        print(dq_action_name)
        if len(dq_action) > 1:
            dq_action_param = dq_action[1]
            print(dq_action_param)
            dq_method = getattr(dq, dq_action_name)
            dq_method(dq_action_param)
            print(dq)
        else:
            dq_action_param = ''
            getattr(dq, dq_action_name)()
    print(' '.join(str(x) for x in dq))


