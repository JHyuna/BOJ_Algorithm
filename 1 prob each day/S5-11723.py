import sys
input = sys.stdin.readline
S = set()
def make_set(order,x):
    global S
    if order == "add":
        if x not in S:
            S.add(x)
    elif order == "remove":
        if x in S:
            S.discard(x)
    elif order == "check":
        if x in S: 
            print(1)
        else : 
            print(0)
    elif order == "toggle":
        if x in S: 
            S.discard(x)
        else: 
            S.add(x)
    elif order == "all" : 
        S = set(list(range(1,21)))
    elif order == "empty" : 
        S = set()

n = int(input())

for _ in range(n):
    order = input().strip()
    if order == "all" or order == "empty" :
        make_set(order,0)
    else : 
        order,x = order.split()
        make_set(str(order),int(x))