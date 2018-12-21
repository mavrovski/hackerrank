from collections import deque


line_numbers = int(input())

deq = deque()

for i in range(0,line_numbers):
    args = input().split()
    command = args[0]
    if(len(args)>1):
        command_arg = int(args[1])
        if(command=='append'):
            deq.append(command_arg)
        elif(command=='appendleft'):
            deq.appendleft(command_arg)
        else:
            raise Exception('Error')
    if(command == 'pop'):
        deq.pop()
    if(command=='popleft'):
        deq.popleft()


print(*list(deq),sep=' ')

