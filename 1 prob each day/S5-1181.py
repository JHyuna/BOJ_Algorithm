import sys
n = int(input())
dctn = {}
L = sorted(set(list(sys.stdin.readline().strip() for _ in range(n) )))
len_L = list(map(len, L))

for l in L:
    if len(l) in dctn:
        dctn[len(l)].append(l)
    else:
        dctn[len(l)] = [l]
for k,v in sorted(dctn.items()):
    for e in v:
        print(e)