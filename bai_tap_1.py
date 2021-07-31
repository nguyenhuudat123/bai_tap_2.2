import math

a = float(input('nhap so a = '))
b = float(input('nhap sp b = '))
c = float(input('nhap so c = '))

delta = b*b - 4*a*c
if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
else:
    x_real = -b/(2*a)
    x_imag = math.sqrt(-delta)/ (2*a)
    x1 = complex(x_real, x_imag)
    x2 = complex(x_real, -x_imag)
print(f'2 nghiem cua phuong trinh la {x1}, {x2}')