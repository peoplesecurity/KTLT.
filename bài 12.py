# Nhập hệ số
a1 = float(input("Nhập a1: "))
b1 = float(input("Nhập b1: "))
c1 = float(input("Nhập c1: "))

a2 = float(input("Nhập a2: "))
b2 = float(input("Nhập b2: "))
c2 = float(input("Nhập c2: "))

# Tính định thức
D = a1 * b2 - a2 * b1
Dx = c1 * b2 - c2 * b1
Dy = a1 * c2 - a2 * c1

# Xét các trường hợp
if D != 0:
    x = Dx / D
    y = Dy / D
    print("Hệ có nghiệm duy nhất:")
    print("x =", round(x,2))
    print("y =", round(y,2))
else:
    if Dx == 0 and Dy == 0:
        print("Hệ có vô số nghiệm")
    else:
        print("Hệ vô nghiệm")