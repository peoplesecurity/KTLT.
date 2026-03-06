import datetime

d = int(input())
m = int(input())
y = int(input())

try:
    date = datetime.date(y, m, d)
    print("Hợp lệ")
    print("Thứ:", date.strftime("%A"))
except:
    print("Không hợp lệ")