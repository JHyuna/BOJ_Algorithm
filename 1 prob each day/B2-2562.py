t = list(int(input()) for _ in range(9))
print('{}\n{}'.format(max(t), t.index(max(t))+1 ))   