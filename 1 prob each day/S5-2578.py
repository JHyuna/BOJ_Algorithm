def make_list(empty):
    for _ in range(5):
        empty += list(map(int, input().split()))
    return empty

board = make_list([])
removed = make_list([])
idx = 0

while True:
    board[board.index(removed[idx])] = 0
    idx += 1

    horz = [board[i:i + 5] for i in range(0, 25, 5)]
    vert = [[horz[i][j] for i in range(5)] for j in range(5)]
    diagonal_1 = [horz[i][i] for i in range(5)]
    diagonal_2 = [horz[i][j] for i,j in zip(range(5), range(4,-1,-1))]
    
    bingo = horz.count([0,0,0,0,0]) + vert.count([0,0,0,0,0])
    if sum(diagonal_1) == 0:
        bingo += 1
    if sum(diagonal_2) == 0:
        bingo += 1
    
    if bingo >= 3:
        print(idx)
        break
