from itertools import combinations
n,m = map(int, input().split())
L = list(map(int, input().split()))
comb_L = [sum(e) for e in list(combinations(L,3)) if sum(e)<=m]
print(max(comb_L))