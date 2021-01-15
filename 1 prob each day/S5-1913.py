n=int(input())
m=int(input())
a=[]
for _ in range(n):
  a.append([0]*n)
k=1
x,y=n//2,n//2
a[x][y]=k
for i in range(1,n//2+1):
  for _ in range(2*i-1):
    y-=1
    k+=1
    a[y][x]=k
  for _ in range(2*i-1):
    x+=1
    k+=1
    a[y][x]=k
  for _ in range(2*i):
    y+=1
    k+=1
    a[y][x]=k
  for _ in range(2*i):
    x-=1
    k+=1
    a[y][x]=k
for _ in range(n-1):
  y-=1
  k+=1
  a[y][x]=k
for i in range(n): print(*a[i])
for i in range(n):
  for j in range(n):
    if a[i][j]==m:
      print(i+1,j+1)