#Day 2 - Variables, Strings, and getting Input from users
# Strings basics
## In order to create a string, you can use either single or double quotes.
## "" or '' is empty string but " " or ' ' is a string with a space in it

# Naming value-đặt tên giá trị
# Tên biến bao gồm các ký tự chữ cái, số và dấu gạch dưới.
# Tên biến không được bắt đầu bằng số và không được chứa khoảng trắng.
# Tên biến phân biệt chữ hoa và chữ thường.

# geting values from user - lấy giá trị từ người dùng
# input() function is used to get input from the user.
# name = input("Enter your name: ") # Khi người dùng nhập thì giá trị sẽ được lưu vào biến name
# print("Hello", name) # In ra tên người dùng
#Excercise
#2.1 Ask the user for their name and age, assign them to varlues to two variables, and then print them.
name = input("Enter your name:")
age = input("Enter your age:")
print(f"Your name is {name} and your age is {age}")
