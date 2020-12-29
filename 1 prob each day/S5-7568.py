t = int(input())
a = [input().split() for _ in range(t)]
seq = []
len_a = len(a)
for i in range(len_a):
    cnt = 1
    for j in range(len_a):
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            cnt += 1
    seq.append(cnt)
for i in seq:
    print(i, end=' ')