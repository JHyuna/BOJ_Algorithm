s = int(input())
n = 1
while True:
    if n*(n+1) <= s*2:
        n += 1
    else:
        print(n-1)
        break