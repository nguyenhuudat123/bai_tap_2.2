a = float(input('nhap so bat ki a = '))
b = float(input('nhap so bat ki b = '))
c = float(input('nhap so bat ki c = '))


if 0 < a < b + c and 0 < b < a + c and 0 < c < a + b:
    print("day la 3 canh cua tam giac")
    if a*a == b*b + c*c or b*b == c*c +a*a or c*c == a*a + b*b:
        print("day la tam giac vuong")
    else:
        print("day khong phai tam giac vuong")
else:
    print("day khong phai 3 canh cua tam giac")
