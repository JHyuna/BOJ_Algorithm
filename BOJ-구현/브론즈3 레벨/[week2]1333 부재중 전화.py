n,l,d = map(int, input().split())
t, ans = 0,d
for _ in range(n):
    if t<=ans<t+l:
        while ans<t+l:ans+=d
    if t+l<=ans<t+l+5:
        break
    t+=l+5
print(ans)