# 2460. 지능형 기차 2
# tuple people의 각 원소 (a,b)에 대해 반복적으로 a를 빼고, b를 더함
# 연산 이후 이를 빈 리스트에 추가. 가장 마지막에 max 출력

L = [list(map(int, input().split())) for _ in range(10)]
p = []
for i in range(10):
    p.insert(i, L[i][1]-L[i][0])
p_state = [sum(p[:i+1]) for i in range(10)]
print(max(p_state))