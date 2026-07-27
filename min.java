# Nhập số lượng phần tử
a = int(input("Nhập số lượng phần tử: "))

# Khởi tạo danh sách
numbers = []

# Nhập các phần tử
for i in range(a):
    num = int(input(f"Nhập phần tử thứ {i + 1}: "))
    numbers.append(num)

# Tìm giá trị nhỏ nhất
min_value = numbers[0]

for num in numbers:
    if num < min_value:
        min_value = num

# In kết quả
print("Dãy số đã nhập:", numbers)
print("Giá trị nhỏ nhất là:", min_value)