import sys
alpb_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
alpb_list = []
ans = 0
temp = []
n = int(sys.stdin.readline())

for _ in range(n):
    alpb = input()
    temp.append(alpb)

for alpb in temp:
    for i in range(len(alpb)):
        num = 10 ** (len(alpb) - i - 1)
        alpb_dict[alpb[i]] += num

for value in alpb_dict.values():
    if value > 0:
        alpb_list.append(value)

sorted_list = sorted(alpb_list, reverse=True)

for i in range(len(sorted_list)):
    ans += sorted_list[i] * (9 - i)

print(ans)