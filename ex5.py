# --- ĐỊNH NGHĨA CÁC HÀM ---

def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b == 0:
        return "Lỗi chia cho 0"
    else:
        return a / b

def hien_thi_menu():
    print("\n--- CALCULATOR BOT MENU ---")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Thoát")

# --- LUỒNG THỰC THI CHÍNH (MAIN) ---

while True:
    hien_thi_menu()
    lua_chon = input("Nhập lựa chọn của bạn (1-5): ")

    # Kiểm tra nếu chọn thoát
    if lua_chon == '5':
        print("Cảm ơn bạn đã sử dụng Calculator Bot. Tạm biệt!")
        break
    
    # Kiểm tra lựa chọn hợp lệ từ 1 đến 4
    if lua_chon in ['1', '2', '3', '4']:
        try:
            # Nhập hai số a và b
            a = float(input("Nhập số a: "))
            b = float(input("Nhập số b: "))

            if lua_chon == '1':
                print(f"Kết quả: {a} + {b} = {cong(a, b)}")
            elif lua_chon == '2':
                print(f"Kết quả: {a} - {b} = {tru(a, b)}")
            elif lua_chon == '3':
                print(f"Kết quả: {a} * {b} = {nhan(a, b)}")
            elif lua_chon == '4':
                ket_qua = chia(a, b)
                if ket_qua == "Lỗi chia cho 0":
                    print(ket_qua)
                else:
                    print(f"Kết quả: {a} / {b} = {ket_qua}")
        except ValueError:
            print("Lỗi: Vui lòng nhập số hợp lệ!")
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại (1-5).")