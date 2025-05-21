numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
numbers.append(5)
print(id(numbers))
print(id(new_numbers))

# Yêu cầu ng dùng nhập 1 số, cho họ biết số đó âm, dương hay bằng 0
number = int(input("Please enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#Trả tiền làm thêm giờ
hours = int(input("Please enter your hours_worked: "))
hourly_wage = 30
if hours > 40:
    overtime = hours - 40
    wage = overtime * hourly_wage * 1.1 + 40 * hourly_wage
    print(f"You are due some additional pay!, and your wage is {wage}" )
else:
    wage = hours * hourly_wage
    print(f"Your wage is {wage}")