n = sorted(list(input()), reverse=True)
if '0' in n and sum(map(int, n))%3 == 0:
    print(''.join(n))
else:
    print(-1)
