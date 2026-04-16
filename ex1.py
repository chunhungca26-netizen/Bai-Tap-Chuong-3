so_km = float(input("Nhập số km đã đi: "))

# Khởi tạo biến tổng tiền
tong_tien = 0

# Tính toán dựa trên các mốc khoảng cách
if so_km <= 0:
    tong_tien = 0
elif so_km <= 1:
    # 1 km đầu tiên
    tong_tien = so_km * 15000
elif so_km <= 20:
    # 1 km đầu + các km từ 2 đến 20
    tong_tien = 1 * 15000 + (so_km - 1) * 12000
else:
    # 1 km đầu + 19 km tiếp theo + các km từ 21 trở đi
    tong_tien = 1 * 15000 + 19 * 12000 + (so_km - 20) * 10000

# In ra số tiền khách phải trả
print(f"Số tiền khách phải trả là: {tong_tien:,.0f} VNĐ")