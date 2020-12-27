TP = list(int(input()) for _ in range(8))
st_TP = sorted(TP)
ans = []
for i in range(3,8):
    ans.append(TP.index(st_TP[i])+1)
print(sum(st_TP[3:]))
print(' '.join(map(str,sorted(ans))))