from collections import Counter
ans = 0
test = int(input())
for i in range(test):
    string = ''
    word = input()
    for k,v in Counter(word).items():
        string += k*v
        if string == word:
            ans+=1
print(ans)