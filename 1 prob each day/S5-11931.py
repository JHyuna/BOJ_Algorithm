import sys
input = sys.stdin.readline
n = int(input())
L = sorted(list(int(input()) for _ in range(n)), reverse=True)
for l in L:
    print(l)