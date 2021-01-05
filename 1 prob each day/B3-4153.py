while True:
    in_value = input()
    if in_value != '0 0 0':
        L = sorted(tuple(map(int, in_value.split())))
        if L[-1]**2 == (L[0]**2 + L[1]**2):
            print('right')
        else:
            print('wrong')
    else:
        break
    