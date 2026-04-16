# 1. Hàm thêm liên hệ mới
def add_contact(danh_ba):
    ten = input("Nhập tên liên hệ: ")
    sdt = input("Nhập số điện thoại: ")
    # Nối chuỗi theo định dạng "Tên - Số điện thoại"
    lien_he = f"{ten} - {sdt}"
    danh_ba.append(lien_he)
    print("Thêm liên hệ thành công!")

# 2. Hàm hiển thị tất cả danh bạ
def show_contacts(danh_ba):
    if not danh_ba:
        print("Chưa có liên hệ nào.")
    else:
        print("\n--- DANH SÁCH LIÊN HỆ ---")
        # Dùng enumerate để in kèm số thứ tự (bắt đầu từ 1)
        for i, lien_he in enumerate(danh_ba, 1):
            print(f"{i}. {lien_he}")

# 3. Hàm tìm kiếm liên hệ (Trong đề ghi là Contacts, mình đặt đúng tên để bạn nộp bài)
def Contacts(danh_ba):
    ten_tim_kiem = input("Nhập tên cần tìm: ")
    found = False
    for lien_he in danh_ba:
        # Kiểm tra xem tên có tồn tại bên trong chuỗi liên hệ không
        if ten_tim_kiem.lower() in lien_he.lower():
            print(f"Thông tin: {lien_he}")
            found = True
    
    if not found:
        print("Không tìm thấy.")

# 4. Hàm main điều phối tổng thể
def main():
    my_contacts = [] # Khởi tạo trạng thái ban đầu rỗng
    
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ DANH BẠ ===")
        print("1. Thêm liên hệ mới")
        print("2. Hiển thị tất cả danh bạ")
        print("3. Tìm kiếm liên hệ")
        print("4. Thoát")
        
        lua_chon = input("Chọn chức năng (1-4): ")
        
        if lua_chon == '1':
            add_contact(my_contacts)
        elif lua_chon == '2':
            show_contacts(my_contacts)
        elif lua_chon == '3':
            Contacts(my_contacts)
        elif lua_chon == '4':
            print("Đang thoát chương trình...")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

# Chạy chương trình
if __name__ == "__main__":
    main()