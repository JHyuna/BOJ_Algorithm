import sys
n = int(input())
nb = sys.stdin.readline
n_list = [0 for i in range(10000+1)]

for _ in range(n):
    n_list[int(nb())] += 1

for i in range(10000):
    for j in range(n_list[i]):
        print(i)