import random

# Máy chọn ngẫu nhiên
choices = ["b", "d", "k"]
computer = random.choice(choices)

# Người chơi nhập
player = input("Nhập b (bao), d (đá), k (kéo): ")

# Kiểm tra nhập sai
if player not in choices:
    print("Nhập sai ký tự!")
else:
    print("Bạn chọn:", player)
    print("Máy chọn:", computer)

    if player == computer:
        print("Hòa!")
    elif (player == "b" and computer == "d") or \
         (player == "d" and computer == "k") or \
         (player == "k" and computer == "b"):
        print("Bạn thắng!")
    else:
        print("Máy thắng!")