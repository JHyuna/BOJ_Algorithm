n = int(input())
L = tuple(map(int, input().split()))
max_v = max(L)
ans = [e/max_v*100 for e in L]
print(sum(ans)/n)