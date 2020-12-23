t = int(input())
for _ in range(t):
    w = input().split('X')
    ans = 0
    for e in w:
        n = len(e)
        ans += n*(n+1)*0.5 # 1부터 n까지의 합의 공식 사용
    print(int(ans))