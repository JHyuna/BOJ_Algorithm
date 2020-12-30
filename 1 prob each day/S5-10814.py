import sys
n = int(input())
L = [tuple(sys.stdin.readline().split()) for _ in range(n)]
L = sorted(L, key=lambda x: (int(x[0]), x[0] ))
for e in L:
    print(' '.join(e))