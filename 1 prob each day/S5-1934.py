from collections import deque
test = int(input())

for _ in range(test):
    a, b = map(int, input().split())
    n = 1
    ans = deque()
    while n <= min(a,b):
        if a % n ==0 and b % n ==0:
            ans.append(n)
            n += 1
        else:
            n += 1
    M = max(ans)
    print(int(M*(a/M)*(b/M)))