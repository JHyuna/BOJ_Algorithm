n = int(input())
fibo_dict = {0:0, 1:1}
def fibonacci(n):
    if n in fibo_dict:
        return fibo_dict[n]
    else:
        ans = fibonacci(n-1) + fibonacci(n-2)
        fibo_dict[n] = ans
        return ans
print(fibonacci(n))