# Nhập số nguyên dương n
n = int(input("Nhập vào một số nguyên dương n: "))

# Khởi tạo các biến tích lũy
tong_le = 0
tong_chan = 0

# Sử dụng vòng lặp for để duyệt qua các số từ 1 đến n
for i in range(1, n + 1):
    if i % 2 == 0:
        # Nếu chia hết cho 2 thì là số chẵn
        tong_chan += i
    else:
        # Nếu không chia hết cho 2 thì là số lẻ
        tong_le += i

# In kết quả ra màn hình
print(f"Tổng các số lẻ từ 1 đến {n} là: {tong_le}")
print(f"Tổng các số chẵn từ 1 đến {n} là: {tong_chan}")