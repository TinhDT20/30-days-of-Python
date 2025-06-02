# Working with files
# opening a file
example_file = open("example.txt")
# example_file = open("copy path") 
# open cấp quyền đọc nhưng không được sửa đổi
print(example_file.read()) #Hello, from the example.txt file!
# đóng tệp
example_file.close()
# có thể tạo 1 tệp mới
write_file = open("write_file.txt", "w") # mở tệp với quyền ghi
write_file.write("Hello, from the write_file.txt file!") # ghi vào tệp
write_file.close()
# việc đóng mở tệp là nhàm chán, python cung cấp 1 công cụ tiện dụng
# đó chính là trình quản lý ngữ cảnh:Context managers
with open("example.txt", "r") as example_file:
    print(example_file.read())
with open("write_file.txt", "w") as write_file:
    write_file.write("\nWelcom to the word!")

# Dữ liệu csv: comma separate values, được biểu thị giống như 1 bảng
# dữ liệu iris
with open("iris.csv", "r") as iris_file:
    # đọc dữ liệu từ tệp
    iris_data = iris_file.read().split("\n") # tách dữ liệu thành các hàng
    # hoặc cách này 
    # iris_data = iris_file.readlines() # đọc từng dòng
irises = []

for row in iris_data[1:]: # bỏ qua hàng(dòng) đầu tiên
    sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(",")
    # Loại bỏ kí tự \n, chia list thành các tuple

    iris_dict = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
        "species": species
    }
    irises.append(iris_dict) # thêm vào danh sách

    # Sử dụng zip
with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()

headers = iris_data[0].strip().split(",")
irises = []

for row in iris_data[1:]:
    iris = row.strip().split(",")
    iris_dict = dict(zip(headers, iris))
    # zip() sẽ tạo ra 1 tuple với các phần tử tương ứng 
    irises.append(iris_dict)
