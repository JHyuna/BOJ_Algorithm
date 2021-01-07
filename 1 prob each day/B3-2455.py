L = [list(map(int, input().split())) for _ in range(4)]
p = []
for i in range(4):
    p.insert(i, L[i][1]-L[i][0])
p_state = [sum(p[:i+1]) for i in range(4)]
print(max(p_state))