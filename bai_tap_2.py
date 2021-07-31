import math

while True:
    n = int(input('nhap so nguyen duong n: '))
    if n > 0:
        break
    print("nhap sai, nhap lai số NGUYÊN DƯƠNG n: ")

x = float(input("nhap so thuc x bat ki: "))

s_1 = 0
for i in range(n + 1):
    s_1 += pow(x, i)

s_2 = 0
for i in range(n + 1):
    s_2 += pow(-1, i) * pow(x, i)


def giai_thua(k):
    if k == 0:
        return 1
    return giai_thua(k - 1) * k


s_3 = 0
for i in range(n + 1):
    s_3 += pow(x, i) / giai_thua(i)

print(s_1)
print(s_2)
print(s_3)