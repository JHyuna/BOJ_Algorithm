import sys
from collections import deque

# 10845번처럼 list로 구현 시 시간초과, deque로 시간 단축 필요

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
        return queue.popleft()
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

dq = deque()
n = int(input())
for _ in range(n):
    input_s = sys.stdin.readline().rstrip().split()
    order = input_s[0]
    if order == 'push':
        push(dq, input_s[1])
    elif order == 'pop':
        print(pop(dq))
    elif order == 'size':
        print(size(dq))
    elif order == 'empty':
        print(empty(dq))
    elif order == 'front':
        print(front(dq))
    else:
        print(back(dq))