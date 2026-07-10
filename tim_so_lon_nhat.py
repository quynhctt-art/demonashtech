# -*- coding: utf-8 -*-
"""
Chương trình: Tìm số lớn nhất (Maximum Value Finder)
Ngôn ngữ: Python 3
Mô tả: Cung cấp các phương pháp tìm số lớn nhất từ cơ bản đến nâng cao,
       có tích hợp tương tác với người dùng.
"""

def tim_max_ba_so(a, b, c):
    """
    Cách 1: Sử dụng cấu trúc điều kiện if-else (Tư duy logic cơ bản)
    """
    so_lon_nhat = a
    if b > so_lon_nhat:
        so_lon_nhat = b
    if c > so_lon_nhat:
        so_lon_nhat = c
    return so_lon_nhat


def tim_max_danh_sach(danh_sach):
    """
    Cách 2: Sử dụng hàm max() tích hợp sẵn của Python (Tối ưu, ngắn gọn)
    """
    if not danh_sach:
        return None
    return max(danh_sach)


def main():
    print("=" * 50)
    print("CHƯƠNG TRÌNH SO SÁNH VÀ TÌM SỐ LỚN NHẤT")
    print("=" * 50)
    
    # --- THỬ NGHIỆM CÁC HÀM CƠ BẢN ---
    print("\n1. Thử nghiệm với các số cố định:")
    x, y, z = 15, 27, 20
    print(f"   Các số thử nghiệm: a = {x}, b = {y}, c = {z}")
    print(f"   => Số lớn nhất (dùng if-else): {tim_max_ba_so(x, y, z)}")
    
    ds_mau = [45, 78, 12, 99, 34]
    print(f"   Danh sách mẫu: {ds_mau}")
    print(f"   => Số lớn nhất (dùng hàm max): {tim_max_danh_sach(ds_mau)}")
    
    print("\n" + "-" * 50)
    
    # --- TƯƠNG TÁC VỚI NGƯỜI DÙNG ---
    print("2. Chạy chương trình tương tác thực tế:")
    try:
        nhap_vao = input("Nhập các số cần so sánh (cách nhau bằng dấu cách): ")
        
        # Chuyển chuỗi nhập vào thành danh sách các số thực (float) để hỗ trợ cả số thập phân
        cac_so = [float(x) for x in nhap_vao.split()]
        
        if len(cac_so) == 0:
            print(" Bạn chưa nhập số nào!")
        else:
            so_lon_nhat = tim_max_danh_sach(cac_so)
            
            # Định dạng lại hiển thị: nếu là số nguyên thì bỏ phần thập phân .0 đi cho đẹp
            cac_so_hien_thi = [int(n) if n.is_integer() else n for n in cac_so]
            kq_hien_thi = int(so_lon_nhat) if so_lon_nhat.is_integer() else so_lon_nhat
            
            print(f"\n Danh sách số bạn đã nhập: {cac_so_hien_thi}")
            print(f" => SỐ LỚN NHẤT LÀ: {kq_hien_thi}")
            
    except ValueError:
        print(" Lỗi: Vui lòng chỉ nhập các chữ số hợp lệ!")
        
    print("\n" + "=" * 50)
    print("Cảm ơn bạn đã sử dụng chương trình!")

if __name__ == "__main__":
    main()
