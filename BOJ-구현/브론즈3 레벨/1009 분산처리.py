n = int(input())
for _ in range(n):
    a,b = map(int, input().split())
    t = ((a%10)**(b%4+4))%10 # 끝자리에 초점을 두고 계산, 4번마다 반복되므로 진수에 조건포함
    print(10 if t==0 else t)