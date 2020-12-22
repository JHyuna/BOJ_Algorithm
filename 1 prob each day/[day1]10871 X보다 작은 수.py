n,x = map(int, input().split())
a = input().split()
ans = [e for e in a if int(e)<x]
print(' '.join(ans))