n=int(input())
for i in range(n-1,-1,-1):
    string = ' '*(2*i)
    print(string.center(2*n,'*'))
for i in range(1,n):
    string = ' '*(2*i)
    print(string.center(2*n,'*'))