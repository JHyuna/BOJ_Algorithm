n = int(input())
q, r = divmod(n,3)
if q % 2 == 0:
    print('SK' if r == 1 else 'CY')
else:
    print('CY' if r == 1 else 'SK')
