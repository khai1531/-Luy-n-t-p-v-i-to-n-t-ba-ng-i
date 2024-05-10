# Lấy số tiền chi tiêu từ người dùng
so_tien_chi_tieu = float(input("Nhập số tiền bạn đã chi tiêu: "))

# Khởi tạo biến lưu trữ giá trị giảm giá
giam_gia = 0

# Xác định mức giảm giá dựa trên số tiền chi tiêu
if so_tien_chi_tieu < 75:
    giam_gia = 0
elif so_tien_chi_tieu < 100:
    giam_gia = so_tien_chi_tieu * 0.15
elif so_tien_chi_tieu < 150:
    giam_gia = so_tien_chi_tieu * 0.25
else:
    giam_gia = so_tien_chi_tieu * 0.5

# Tính toán tổng số tiền cần thanh toán
tong_tien_thanh_toan = so_tien_chi_tieu - giam_gia

# In ra thông tin hóa đơn
print(f"Số tiền bạn đã chi tiêu: ${so_tien_chi_tieu:.2f}")
print(f"Mức giảm giá: ${giam_gia:.2f}")
print(f"Tổng số tiền cần thanh toán: ${tong_tien_thanh_toan:.2f}")