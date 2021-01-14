from collections import Counter
X,Y = [], []

for i in range(3):
    x,y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(3):
    if X.count(X[i]) == 1:
        ans_x = X[i]
    if Y.count(Y[i]) == 1:
        ans_y = Y[i]
    
print(ans_x,ans_y)
