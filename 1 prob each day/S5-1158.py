n,k = map(int, input().split())
L = list(range(1,n+1))
idx = 0
ans = []

for i in range(n):
    idx += k-1
    if idx >= len(L):
        idx = idx%len(L)
    ans.append(str(L.pop(idx)))
print("<",", ".join(ans),">", sep='')