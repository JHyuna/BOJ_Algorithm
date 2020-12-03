D = {'0':4, '1':2}
while True:
  a = input()
  l = 2 + len(a) - 1
  if a!='0':
    for i in range(len(a)):
      if a[i] in D.keys() : l += D[a[i]]
      else : l += 3
    print(l)
  else : break