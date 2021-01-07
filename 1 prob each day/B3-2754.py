grade_dict = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0}
sign_dict = {'+':0.3, '0':0, '-':-0.3}
grade = input()
ans = 0
if grade == 'F': 
    print(0.0)
else:
    ans += grade_dict[grade[0]]
    ans += sign_dict[grade[1]]
    print(ans)