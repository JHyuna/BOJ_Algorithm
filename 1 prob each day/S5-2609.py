from collections import deque
a, b = map(int, input().split())
if max(a,b) % min(a,b) == 0:
    print('{}\n{}'.format(min(a,b),max(a,b)))
else:
    n = 1
    ans = deque()
    while n <= min(a,b):
        if a % n ==0 and b % n ==0:
            ans.append(n)
            n += 1
        else:
            n += 1
    M = max(ans)
    print(M)
    print(int(M*(a/M)*(b/M)))




