n = int(input())
h = 0
for i in range(1, n+1):
    if i<100:
        h+=1
    else:
        L = list(map(int, str(i)))
        if L[0]-L[1] == L[1]-L[2]:
            h += 1
print(h)