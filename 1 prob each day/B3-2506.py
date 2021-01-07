number = input()
L = input().replace(' ','').split('0')
ans = 0
for l in L:
    n = len(l)
    ans += 0.5*n*(n+1)
print(int(ans))