#Credit Card Validator
# Số đầu tiên bên phải của thẻ là số kiểm tra
# Số kiểm tra được tính bằng cách nhân các số ở vị trí chẵn với 2, cộng các số ở vị trí lẻ lại với nhau
# Nếu tổng của các số ở vị trí chẵn lớn hơn 9 thì trừ đi 9
# nếu kết quả chia hết cho 10 thì thẻ hợp lệ

seri = list(input("Nhập số thẻ tín dụng: ").strip()) # loại bỏ khoảng trắng, chuyển thành list
temp = seri[:-1]
print (seri)
check_seri = temp [::-1]# lọai số cuối cùng và lật ngược lại 
print(check_seri)
# loại phần tử đầu tiên check_seri = seri[1:]
sum = 0
for i in range(len(check_seri)):
    if i % 2 == 0:
        if int(check_seri[i]) * 2 > 9:
            sum += int(check_seri[i]) * 2 - 9
        else:
            sum += int(check_seri[i]) * 2
    else:
        sum += int(check_seri[i])
print (f"Tổng là: {sum}")
if sum % 10 == 0:
    print("Thẻ hợp lệ")
else:
    print("Thẻ không hợp lệ")
