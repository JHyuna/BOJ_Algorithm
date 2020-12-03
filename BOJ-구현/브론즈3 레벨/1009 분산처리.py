n = int(input())
for _ in range(n):
    a,b = map(int, input().split())
    t = ((a%10)**(b%4+4))%10 # 전체를 다 계산할 필요 없이 끝자리에 집중
    print(10 if t==0 else t)