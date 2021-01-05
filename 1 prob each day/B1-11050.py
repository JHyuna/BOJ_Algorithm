from math import factorial
n,k = map(int, input().split())
nCk = factorial(n)//(factorial(k)*factorial(n-k))
print(nCk)