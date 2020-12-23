L = list(map(int, input().split()))
print('ascending' if L==sorted(L) else 'descending' if L==sorted(L, reverse=True) else 'mixed')