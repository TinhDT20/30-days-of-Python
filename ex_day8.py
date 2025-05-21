import random
print("Welcome to the game of guessing a number between 1 and 100!")
a = random.randint(1, 100)
b = int(input("I have selected a number between 1 and 100. Can you guess it?")) #user_number_selected
while a != b:
    if b < a:
        print("Your number is lower than mine . Try again.") 
    if a < b:
        print("Your number is higher than mine. Try again.")
    b = int(input("Please enter a number between 1 and 100: "))
print("Congratulations! You guessed my number!")
 # Ex2
string = input("Please enter a string: ") #Hello world
chars = list(string)
after_string = []
for i in range(len(chars)):
    if chars[i] == "o":
        continue
    after_string.append(chars[i])
print ("".join(after_string)) #Hell wrld
# Ex3
# In số nguyên tố từ 1 đến 100
list = []
for i in range(0, 101):
    if i < 2:
        continue
    else:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            list.append(i)
print(list)