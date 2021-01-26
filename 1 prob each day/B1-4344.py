case_num = int(input())
answer = []
for k in range(case_num):
    line = list(map(int, input().split()))
    line_avg = sum(line[1:]) / line[0]
    upper_list=[]
    for i in line[1:]:
        if i > line_avg:
            upper_list.append(i)
    answer.append("%0.3f"%round(len(upper_list)/line[0]*100 , 3))
for i in answer:
    print("%s%%"%i)      