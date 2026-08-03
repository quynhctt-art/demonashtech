def find_max(numbers):
    if not numbers:
        raise ValueError("Danh sách không được để trống.")
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum


def main():
    print("=== CHƯƠNG TRÌNH TÌM SỐ LỚN NHẤT ===")
    raw = input("Nhập các số, cách nhau bởi dấu cách: ").strip()
    try:
        numbers = [float(x) for x in raw.split()]
        print(f"Số lớn nhất là: {find_max(numbers)}")
    except ValueError as e:
        print(f"Lỗi: {e}")


if __name__ == "__main__":
    main()
