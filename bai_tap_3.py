import math

while True:
    n_input = float(input("nhap so nguyen duowng n < 1000: n = "))
    if 1000 > n_input > 0 and n_input - math.floor(n_input) == 0:
        break
    print("hay nhap lai. ")

n = int(n_input)


def sum_n(k):
    if k == 0:
        return 0
    return sum_n(k // 10) + k % 10


print(f"tong cac chu so cua so {n} la {sum_n(n)}")

