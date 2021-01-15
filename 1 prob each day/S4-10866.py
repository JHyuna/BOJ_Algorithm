import sys

def push_front(deque, x):
    deque.insert(0,x)

def push_back(deque, x):
    deque.append(x)

def pop_front(deque):
    if empty(deque)==0:
        return deque.pop(0)
    else:
        return -1

def pop_back(deque):
    if empty(deque)==0:
        return deque.pop()
    else:
        return -1

def size(deque):
    return len(deque)

def empty(deque):
    if len(deque)==0:
        return 1
    else:
        return 0

def front(deque):
    if empty(deque)==0:
        return deque[0]
    else:
        return -1

def back(deque):
    if empty(deque)==0:
        return deque[-1]
    else:
        return -1

dq = []
n = int(input())
for _ in range(n):
    input_s = sys.stdin.readline().rstrip().split()
    order = input_s[0]
    if order == 'push_front':
        push_front(dq, input_s[1])
    elif order == 'push_back':
        push_back(dq, input_s[1])
    elif order == 'pop_front':
        print(pop_front(dq))
    elif order == 'pop_back':
        print(pop_back(dq))
    elif order == 'size':
        print(size(dq))
    elif order == 'empty':
        print(empty(dq))
    elif order == 'front':
        print(front(dq))
    else:
        print(back(dq))