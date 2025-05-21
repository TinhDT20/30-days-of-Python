# Fizz Buzz
# Nếu số đó chia hết cho 3, thay vì nói số đó, người chơi phải nói "Fizz".
# Nếu số chia hết cho 5, thay vì nói số đó, người chơi phải nói "Buzz".
# Nếu số đó chia hết cho 3và5 , thay vì nói số đó, người chơi phải nói "Fizz Buzz".

list = []
for number in range(1, 101):
    if (number % 3 == 0 ):
        if(number % 5 == 0): 
            #print("Fizz Buzz")
            list.append("Fizz Buzz")
        else: 
            # print("Fizz")
            list.append("Fizz")
    elif (number % 5 == 0):
        # print("Buzz")
        list.append("Buzz")
    else:
        # print(number)
        list.append(number)
print(list)