# Day3. Formatting Strings and Processing User Input
# 1. String Concatenation
# Dungf toán tử + để nối chuỗi
hourly_wage = input("Please enter your hourly wage: ")
hours_worked = input("How many did you work this week? ")

print ("Hourly wage: " + hourly_wage)
print ("Hour work: " + hours_worked)
# Tuy nhiên, nếu bạn muốn nối các biến kiểu số với nhau, bạn cần chuyển đổi chúng thành chuỗi trước khi nối
# Dùng hàm str để chuyển đổi kiểu số thành chuỗi
# Dùng hàm int, float,... để chuyển đổi chuỗi thành kiểu số
hourly_wage = int(hourly_wage)
hours_worked = int(hours_worked)
print ("Hourly wage: " + str(hourly_wage))
print ("Hour work: " + str(hours_worked))   
# 2. String interpolation
# Khi dùng phương thức format() để định dạng chuỗi, bạn có thể sử dụng các biến trong chuỗi mà không cần phải chuyển đổi chúng thành chuỗi
# Dùng {} để đánh dấu vị trí mà bạn muốn chèn giá trị của biến vào
# Dùng phương thức format() để định dạng chuỗi
print("{} is {} years old".format("John", 30))

output = "{0} is {1} years old, and {0} works as a {2}"
print(output.format("John", 30, "developer"))

output = "{name} is {age} years old, and {name} works as a {job}"
print(output.format(name="John", age=30, job="developer"))

name = "John"
age = 30
job = "developer"
print(f"{name} is {age} years old, and {name} works as a {job}")

# 3. Xử lý chuỗi cơ bản
# lower, upper, title, capitalize, strip
print("Hello World".lower()) # hello world
print("Hello World".upper()) # HELLO WORLD
print("Hello World".title()) # Hello World
print("Hello World".capitalize()) # Hello world
print("   Hello World   ".strip()) # Hello World
user_name = input("Please enter your name: ")
print ("Hello " + user_name.strip().title() + "!")