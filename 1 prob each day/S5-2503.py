import sys
import itertools

def func(n, list):
	sum =0
	for x in itertools.permutations([1,2,3,4,5,6,7,8,9],3):
		a,b,c = x
		for i in range(n):
			st = 0
			ba = 0
			temp = list[i][0]
			temp_a = temp//100
			temp_b = temp//10 % 10
			temp_c = temp%10
			
			if temp_a == a:
				st += 1
			if temp_b == b:
				st += 1
			if temp_c == c:
				st += 1
			if st != list[i][1]:
				break

			if temp_a == b or temp_a == c:
				ba += 1
			if temp_b == a or temp_b == c:
				ba += 1
			if temp_c == a or temp_c == b:
				ba += 1
			if ba != list[i][2]:
				break

			if i == n-1:
				sum += 1
	return sum

n = int(sys.stdin.readline().rstrip())
list=[]
a=[]
for i in range(n):
	a = map(int, sys.stdin.readline().split())
	b = [int(x) for x in a]
	list.append(b)


result = func(n, list)
print(result)