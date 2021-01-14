cnd = [sum(map(int, input().split())) for _ in range(5)]
print(cnd.index(max(cnd))+1, max(cnd))