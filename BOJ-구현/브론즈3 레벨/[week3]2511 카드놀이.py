A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
state=''
for i in range(10):
    a,b = A[i],B[i]
    if a>b:
        state += 'A'
    elif a<b:
        state += 'B'
    else:
        state += 'D'

equal = state.count('D')
total_A = state.count('A')*3 + equal
total_B = state.count('B')*3 + equal
print(total_A, total_B)

if total_A == total_B:
    final_state = state.replace('D','')
    if len(final_state) != 0:
        print(state.replace('D','')[-1])
    else:
        print('D')
elif total_A > total_B : print('A')
else : print('B')