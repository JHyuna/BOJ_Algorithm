# 피보나치수 구하기
# 재귀 + 메모라이징 // 더 빠른 풀이도 생각해보자
d = {0:0, 1:1, 2:1}
n = int(input())
def fibonacci(n):
    if n in d:
        ans = d[n]
    else:
        d[n] = fibonacci(n-1) + fibonacci(n-2)
        ans = d[n]
    return ans
print(fibonacci(n))