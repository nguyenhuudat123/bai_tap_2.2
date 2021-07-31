def giai_thua(k):
    if k == 0:
        return 1
    return giai_thua(k - 1) * k


while True:
    epsilon = float(input("nhap so epsilon < : epsilon = "))
    if epsilon < 1:
        break
    print('moi nhap lai epsilon ---> ')

if epsilon <= 0:
    print('n khong xac dinh')
else:
    i = 0
    e = 1
    while 1 / giai_thua(i) >= epsilon:
        i += 1
        e += 1 / giai_thua(i)
    print(f'e = {e}')
