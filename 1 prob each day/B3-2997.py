a,b,c = sorted(map(int, input().split()))
ab, bc = b-a, c-b
if ab == bc:
    ans = c + ab
elif ab > bc:
    ans = int((a+b)/2)
else:
    ans = int((b+c)/2)
print(ans)


