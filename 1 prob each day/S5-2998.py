# 문자열 replace 방식
n = input()
ln = len(n)
n_list = []

if ln % 3 ==0: # 문자열을 일정 길이로 나누는 건 아래처럼 map으로 하는 것도 가능
    pass
else:
    n = '0'*(3-(ln%3)) + n

for i in range(0, ln, 3):
    a = n[i:i+3]
    if a in ['000','001']:
        b = oct(int(a.replace('00','0b'),2)).replace('0o','')
        n_list.append(b)
    elif a in ['010','011']:
        b = oct(int('0b' + a[1:], 2)).replace('0o','')
        n_list.append(b)
    else:
        b = oct(int('0b' + a,2)).replace('0o','')
        n_list.append(b)
print(int(''.join(n_list)))

# dictionary 이용
dic_8 = {'000':'0', '001':'1', '010':'2', '011':'3','100':'4','101':'5','110':'6','111':'7'}
n = input()
ln = len(n)
if ln % 3 ==0:
    pass
else:
    n = '0'*(3-(ln%3)) + n

n_list = list(map(''.join, zip(*[iter(n)]*3)))
ans = [dic_8[e] for e in n_list]
print(int(''.join(ans)))

    