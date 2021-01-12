import sys
n = int(input())
L = sorted(list(int(sys.stdin.readline()) for _ in range(n)))

print(round(sum(L)/n))
print( L[(n-1)//2] )

from collections import Counter
L_cnt=Counter(L).most_common()
if n > 1: 
    if L_cnt[0][1] == L_cnt[1][1]:print(L_cnt[1][0]) 
    else : print(L_cnt[0][0]) 
else : print(L[0]) 

print(max(L)-min(L))
