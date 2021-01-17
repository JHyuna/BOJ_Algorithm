import sys
n = int(input())
nums = [sys.stdin.readline().split() for _ in range(n)]
for nm in nums:
    ans = []
    for e in nm:
        ans.append(e[::-1])
    print(' '.join(ans))