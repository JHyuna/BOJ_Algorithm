n, m, k = map(int, input().split())
cnt = 0
while n >= 0 and m >= 0 and n + m >= k:
    n -= 2
    m -= 1
    cnt += 1
print(cnt - 1)