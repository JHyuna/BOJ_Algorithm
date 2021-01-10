n = int(input())
bg_paper = [[0]*100 for _ in range(100)]
area = 0

for _ in range(n):
    x,y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            bg_paper[i][j] = 1
            
for line in bg_paper:
    area += sum(line)
print(area)