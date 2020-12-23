t = int(input())
for _ in range(t):
    n,word = input().split()
    string = ''
    for w in word:
        string += int(n)*w
    print(string)