test = int(input())
for i in range(test):
    h,w,n = map(int, input().split())
    index_w, index_h = divmod(n,h)
    if index_h ==0:
        print(str(h) + str(index_w).zfill(2))
    else:
        print(str(index_h) + str(index_w+1).zfill(2))