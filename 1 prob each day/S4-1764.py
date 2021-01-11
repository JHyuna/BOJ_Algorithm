db, bd = map(int, input().split())
db_dict = {}
db_list = sorted(list(input() for _ in range(db)))
for i in db_list:
    db_dict[i] = 0

for j in range(bd):
    p = input()
    if p in db_dict:
        db_dict[p] = 1

print(sum(db_dict.values()))
for k,v in db_dict.items():
    if v == 1: print(k)