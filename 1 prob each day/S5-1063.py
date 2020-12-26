# 문제이름 : 킹
import string

king, stone, moving = input().split()
king = string.ascii_uppercase.index(king[0]) + 1, int(king[1])
stone = string.ascii_uppercase.index(stone[0]) + 1, int(stone[1])
moving_list = [input() for _ in range(int(moving))]

transfer = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1),
            'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}

for key in moving_list:
    moved_king = tuple(sum(e) for e in zip(king, transfer[key]))

    if not (0 < moved_king[0] < 9 and 0 < moved_king[1] < 9):  # 판을 벗어나면 패스, 다음이동 수행
        continue
    if moved_king == stone:
        moved_stone = tuple(sum(e) for e in zip(stone, transfer[key]))

        if not (0 < moved_stone[0] < 9 and 0 < moved_stone[1] < 9):
            continue
        king, stone = moved_king, moved_stone
    else:
        king = moved_king

print(string.ascii_uppercase[king[0] - 1] + str(king[1]))
print(string.ascii_uppercase[stone[0] - 1] + str(stone[1]))