# 1. Định nghĩa hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    # Vòng lặp kiểm tra từ 2 đến n-1
    for i in range(2, n):
        if n % i == 0:
            return False  # Nếu chia hết cho số nào đó thì không phải số nguyên tố
    return True

# 2. In ra tất cả các số nguyên tố từ 1 đến 100
print("Các số nguyên tố từ 1 đến 100 là:")
for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")