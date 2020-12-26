# 시간초과된 풀이
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

# 수정한 풀이 : python3대신 PyPy3사용
# input()의 경우 다량의 입력이 발생하면 python3 말고 pipy3로 제출해야 함
from sys import stdin
n = int(input())
T = sorted(map(int,stdin) for _ in range(n))
for i in T:
    print(i)

# 참고할 풀이
# input()보다는 stdin이 훨씬 빠르다.
import sys
n = int(input())
nums = sorted([int(sys.stdin.readline()) for _ in range(n)])
for e in nums : print(e)