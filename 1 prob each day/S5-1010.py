import operator as op
from functools import reduce

def nCr(r,n):
    if n<1 or r<0 or n<r:
        raise ValueError
    r = min(r,n-r)
    nm = reduce(op.mul, range(n,n-r,-1),1)
    dm = reduce(op.mul, range(1, r+1),1)
    return nm//dm

case = int(input())
for _ in range(case):
    R,N = map(int, input().split())
    print(nCr(R,N))