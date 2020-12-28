import sys
n = int(input())
nums = set(map(int,sys.stdin.readline().split()))
print(' '.join(map(str,sorted(nums))))