import sys
n = int(input())
nums = [tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]
sorted_nums = sorted(nums, key = lambda x: (x[1], x[0]))
for e in sorted_nums:
    print(' '.join(map(str,e)))