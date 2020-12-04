dic = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
while True:
    l = input().rstrip()
    if l=='#':break
    t = 0
    for i in range(len(l)):
        t += dic.get(l[i])*(8**(len(l)-i-1))
    print(t)