# Conditionals and Booleans
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True do hai danh sách này bằng nhau
print(a is b)  # False do chúng không phải là cùng một đối tượng

## id in ra địa chỉ của biến 
print(id(a))  # id của a
print(id(b))  # id của b
# hai biến này có cùng giá trị nhưng không phải là cùng một đối tượng
# vì vậy id của chúng khác nhau

# c = a 
# print(a == b)  # True
# print(a is b)  # True, lúc này hai biến cùng 1 địa chỉ

# Câu lệnh có điều kiện
age = int(input("How old are you? "))

if age < 18:
    print("Sorry, we can't serve you")
else:
    chosen_drink = input("What can I get for you? ")
## elseif: