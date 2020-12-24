w_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
obj = input()
for w in w_list:
    if w in obj:
        # w_list내의 문자는 *로 치환, 크로아티아 알파벳아 아닌 문자는 그대로 남김
        obj = obj.replace(w,'*')
print(len(obj))