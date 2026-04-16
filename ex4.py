# 1. Hàm tìm số lớn nhất
def find_max(lst):
    if not lst:
        return None
    max_val = lst[0]  # Giả sử phần tử đầu tiên là lớn nhất
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val

# 2. Hàm tìm số nhỏ nhất
def find_min(lst):
    if not lst:
        return None
    min_val = lst[0]  # Giả sử phần tử đầu tiên là nhỏ nhất
    for x in lst:
        if x < min_val:
            min_val = x
    return min_val

# 3. Chạy thử nghiệm với mảng diem_so
diem_so = [6.5, 8.0, 4.5, 9.5, 7.0]

max_diem = find_max(diem_so)
min_diem = find_min(diem_so)

print(f"\nDanh sách điểm: {diem_so}")
print(f"Điểm lớn nhất: {max_diem}")
print(f"Điểm nhỏ nhất: {min_diem}")