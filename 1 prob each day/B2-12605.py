n = int(input())
for i in range(1,n+1):
    string = reversed(input().rstrip().split())
    print('Case #' + str(i) + ': ' + ' '.join(string))

