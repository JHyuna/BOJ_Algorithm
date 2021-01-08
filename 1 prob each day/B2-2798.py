from itertools import combinations
n,m = map(int, input().split())
L = list(map(int, input().split()))
comb_L = [sum(e) for e in list(combinations(L,3)) if sum(e)<=m]
print(max(comb_L))

    # 저장해놓기. comp
    # 새로 구한 sum(e)-m과 comp비교
    # comp가 더 작으면 