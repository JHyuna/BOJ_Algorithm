a,b = map(int, input().split())
c,d = map(int, input().split())
L = [c*d, d*b, a*b, a*c]
print(L.index(min(L)))