conv = [tuple(map(int, input().split()))]
ans = []
n = int(input())
for _ in range(n):
    conv.append(tuple(map(int, input().split())))
for i in range(n+1):
    ans.append(1000/conv[i][1]*conv[i][0])
print('%.2f' % min(ans))