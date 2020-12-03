a = [0,1,2,3] # 인덱스활용을 쉽게 하기 위해 1번 컵의 인덱스를 1로 조정
n = int(input())
for _ in range(n):
  i,j = map(int, input().split())
  a[i],a[j] = a[j],a[i]
print(a.index(1)) # 공을 처음에 담은 1번 컵의 위치를 뽑기