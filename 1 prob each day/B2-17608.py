import sys
n = int(input())
stick_list = list(int(sys.stdin.readline()) for _ in range(n))

right = stick_list.pop()
cnt = 1

for i in range(len(stick_list)-1,-1,-1):
    now = stick_list.pop()
    if now > right:
        cnt += 1
        right = now
    else:
        pass

print(cnt)


# stack 구현 참고한 풀이 ↓
import sys
stick = sys.stdin.readline

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
        a = stack.pop()
        return a
    else:
        return -1

def top(stack):
    if empty(stack)==0:
        return stack[len(stack)-1]
    else:
        return -1
    
n = int(input())
stk = list()
max_s, cnt = 0,0

for _ in range(n):
    push(stk, int(stick))

for i in range(len(stk)-1, -1, -1):
    if stk[i] > max_s:
        cnt += 1
        max_s = stk[i]
print(cnt)
         



