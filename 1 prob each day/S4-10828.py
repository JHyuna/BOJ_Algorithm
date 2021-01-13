import sys

def size(stack):
    return len(stack)

def empty(stack):
    if len(stack)==0:
        return 1
    else:
        return 0

def push(stack, x):
    stack.append(x)

def pop(stack):
    if empty(stack)==0:
        return stack.pop()
    else:
        return -1

def top(stack):
    if empty(stack)==0:
        return stack[len(stack)-1]
    else:
        return -1

stk = []
n = int(input())
for _ in range(n):
    input_s = sys.stdin.readline().rstrip().split()
    order = input_s[0]
    if order == 'push':
        push(stk, input_s[1])
    elif order == 'pop':
        print(pop(stk))
    elif order == 'size':
        print(size(stk))
    elif order == 'empty':
        print(empty(stk))
    else:
        print(top(stk))

        

