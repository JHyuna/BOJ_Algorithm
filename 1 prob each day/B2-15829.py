n, letters = int(input()), input()
numbers = [ord(letter) - 96 for letter in letters]
nm_sum = 0
for i in range(n):
    nm_sum += numbers[i]*(31**i)
print(nm_sum % 1234567891)