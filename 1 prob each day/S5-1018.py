import sys

def check_BW(matrix):
    case1_not_match = 0
    case2_not_match = 0

	# case 1 시작점(0,0)이 W 인경우 
    for x in range(8):
        for y in range(8):
            if ((x % 2 == 0) and (y % 2 == 0)) or ((x % 2 == 1) and (y % 2 == 1)):  # 행짝 열짝, 행홀 열홀
                if matrix[x][y] != "W":
                    case1_not_match += 1

            elif ((x % 2 == 1) and (y % 2 == 0) or (x % 2 == 0) and (y % 2 == 1)):  # 행홀 열짝, 행짝 열홀
                if matrix[x][y] != "B":
                    case1_not_match += 1
	
    # case 2 시작점(0,0)이 B 인경우 
    for x in range(8):
        for y in range(8):
            if ((x % 2 == 0) and (y % 2 == 0)) or ((x % 2 == 1) and (y % 2 == 1)):  # 행짝 열짝, 행홀 열홀
                if matrix[x][y] != "B":
                    case2_not_match += 1

            elif ((x % 2 == 1) and (y % 2 == 0) or (x % 2 == 0) and (y % 2 == 1)):  # 행홀 열짝, 행짝 열홀
                if matrix[x][y] != "W":
                    case2_not_match += 1

    return min(case1_not_match, case2_not_match)

def solution():
    input_list = []
    M, N = map(int, sys.stdin.readline().split())
    for idx in range(M):
        input_list.append([i for i in sys.stdin.readline()][:-1])

    min_revise_cnt = 123041234723842
    for row in range(M-7):
        for col in range(N-7):
        	# 8*8 매트릭스로 자르기
            slice_mat = [one_row[col:col+8] for one_row in input_list[row:row+8]]
            revise_cnt = check_BW(slice_mat)
            min_revise_cnt = min(min_revise_cnt, revise_cnt)

    return min_revise_cnt

print(solution())