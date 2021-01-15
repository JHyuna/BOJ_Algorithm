import sys

def size(queue):
    return len(queue)

def empty(queue):
    if len(queue)==0:
        return 1
    else:
        return 0

def push(queue, x):
    queue.append(x)

def pop(queue):
    if empty(queue)==0:
        return queue.pop(0)
    else:
        return -1

def front(queue):
    if empty(queue)==0:
        return queue[0]
    else:
        return -1

def back(queue):
    if empty(queue)==0:
        return queue[-1]
    else:
        return -1

que = []
n = int(input())
for _ in range(n):
    input_s = sys.stdin.readline().rstrip().split()
    order = input_s[0]
    if order == 'push':
        push(que, input_s[1])
    elif order == 'pop':
        print(pop(que))
    elif order == 'size':
        print(size(que))
    elif order == 'empty':
        print(empty(que))
    elif order == 'front':
        print(front(que))
    else:
        print(back(que))