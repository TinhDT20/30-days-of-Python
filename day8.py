# # Vòng lặp While
# # Dùng loại vòng lặp này khi muốnmuốn đáp ứng nhu cầu điều kiện

# user_number = input ("Please enter a number: ")

# while int(user_number) < 10:
#     print ("Your number is less than 10")
#     user_number = input ("Please enter a number: ")

# print("Your number is greater than or equal to 10")

# Vòng lặp vô hạn
# while True:
#     print("This is an infinite loop")
#     break

while True:
    selected_option = input("Please enter 'a','b','c' or 'q' to quit: ")
    if selected_option == 'a':
        print("You selected option a")
    elif selected_option == 'b':
        print("You selected option b")
    elif selected_option == 'c':
        print("You selected option c")
    elif selected_option == 'q':
        print("You quit the program")
        break
    else:
        print("Invalid option, please try again")

#continue: cho phép bỏ qua phần còn lại của thân vòng lặp hiện tại
# break: cho phép thoát khỏi vòng lặp hiện tại
for number in range(10):
    if number % 2 != 0:
        continue
    print(number)
# 0 2 4 6 8 