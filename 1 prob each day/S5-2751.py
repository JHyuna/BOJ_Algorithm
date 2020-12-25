# 시간초과 뜬다 풀이 고쳐야겠다.
from collections import deque
n,a = int(input()), int(input())
ans = deque([a])
for _ in range(n-1):
    b = int(input())
    if a > b:
        ans.appendleft(b)
    else:
        ans.append(b)
for e in ans: print(e)