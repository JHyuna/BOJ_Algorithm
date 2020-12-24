d = {3:'A', 2:'B', 1:'C', 0:'D', 4:'E'}
for _ in range(3):
    L = tuple(map(int, input().split()))
    sum_L = sum(L)
    print(d[sum_L])