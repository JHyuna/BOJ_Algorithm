n = int(input())
for i in range(n,0,-1):
  print(('*'*i).rjust(n)) # n칸 확보 후 rjust(오른쪽부터 채우기)