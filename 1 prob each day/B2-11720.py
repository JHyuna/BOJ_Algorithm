l,n = tuple(input() for _ in range(2))
ans = 0
for i in range(int(l)):
    ans += int(n[i])
print(ans)