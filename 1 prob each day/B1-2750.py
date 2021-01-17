import sys
n = int(input())
nums = sorted([int(sys.stdin.readline()) for _ in range(n)])
for e in nums : print(e)