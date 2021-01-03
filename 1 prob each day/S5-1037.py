n = int(input())
L = sorted(tuple(map(int, input().split())))
print(L[0]*L[-1])