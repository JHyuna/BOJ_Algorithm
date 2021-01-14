calc = ['+','-','*','/']
nm = input().split()
ans = []
for c in calc:
    ex = nm[0] + c + nm[1]
    ex2 = nm[1] + c + nm[2]
    if eval(ex) == int(nm[2]):
        ans.append(ex + '=' + nm[2])
    if eval(ex2) == int(nm[0]):
        ans.append(nm[0] + '=' + ex2)
print(ans[0])
