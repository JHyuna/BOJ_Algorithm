while True:
  leef = 1
  case = tuple(map(int, input().split()))
  if str(case[0]) != '0':
    for i in range(1,case[0]+1): # i는 1부터 age까지 범위로 조정
      leef *= case[2*i-1] # case 리스트에서 1,3,5...번째 인덱스는 곱해져야 함
      leef -= case[2*i] # case 리스트에서 2,4,5...번째 인덱스는 가지치기이므로 빼야 함
    print(leef)
  else:break