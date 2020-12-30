import sys
n = int(input())
nums = sorted([tuple(map(int,sys.stdin.readline().split())) for _ in range(n)])
for e in nums:
    print(' '.join(list(map(str,e))))