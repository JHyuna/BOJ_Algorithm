# hashing : 200ms
from collections import Counter
n = int(input())
n_cnt = Counter(input().split()).keys()
m = int(input())
m_list = input().split()

for e in m_list:
    print(1 if e in n_cnt else 0)

# dict.fromkeys() : 180ms
n = input()
n_dict = dict.fromkeys(input().split() , 0).keys()
m = input()
m_list = input().split()

for e in m_list:
    print(1 if e in n_dict else 0)

# set : 168ms
n = int(input())
n_list = set(input().split())
m = int(input())
m_list = input().split()

for e in m_list:
    print(1 if e in n_list else 0)


