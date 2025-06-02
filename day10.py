# Dictionary, hoạt đọng hơi khác so với list, string và tuple
# nếu thay đổi vị trí của các phần tử thif điều đó không quan trọng
# vì mỗi giá trị sẽ được liên kết với một key
#một dict có nhiều key nhưng mỗi key là duy nhất, không được trùng nhau
# key có thể là bất kỳ kiểu dữ liệu nào, nhưng thường là string hoặc số
student = {
    "name": "Nguyen Van A",
    "grades": [10 , 9, 8]
}
# các key là name và grade, theo sau là dấu hai chấmchấm
# truy cập vào giá trị của key
print(student["grades"])
# xem key có tồn tại hay không
print(student.get("grades"))

# sửa đổi một dict
student["age"] = 20
# update dict
meta_info = {
    "address": "Hanoi",
    "phone": "0123456789",
    "sex": "male"
}

# cập nhật dict
student.update(meta_info)
print(student)
# sửa các mục hiện có 
student["name"] = "Nguyen Van B"
# xóa một mục
del student["sex"]
#
for key in student:
    print(f"{key}: {student[key]}")
#         #name: Nguyen Van B
          # grades: [10, 9, 8]
            # age: 20
            # address: Hanoi
            # phone: 0123456789
