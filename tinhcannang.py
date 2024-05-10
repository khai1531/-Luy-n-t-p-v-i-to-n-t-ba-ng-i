height = float(input("Nhập vào chiều cao(cm): "))
weight = float(input("Nhập vào cân nặng(kg): "))
BMI = weight / ((height/100)**2)
print(f"Số BMI của bạn là: {BMI}")
if BMI < 16:
    print("Gầy cấp độ III")
elif 16 <= BMI < 17:
    print("Gầy cấp độ II")
elif 17 <= BMI < 18.5:
    print("Gầy cấp độ I")
elif 18.5 <= BMI < 25:
    print("Bình thường")
elif 25 <= BMI:
    print("Thừa cân")
elif 30 <= BMI < 35:
    print("Béo phì cấp độ I")
elif 35 <= BMI < 40:
    print("Béo phì cấp độ II")
else:
    print("Béo phì cấp độ III")