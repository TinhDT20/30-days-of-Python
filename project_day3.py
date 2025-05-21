print("Welcome to the simple earning calculator!")
name = input("What is your name? ")
name = name.strip().title()
print("Hello " + name + "!")
hourly_wage = input("Please enter your hourly wage: ")
hours_worked = input("How many hours did you work this week? ")

earning = int(hourly_wage) * int(hours_worked)  
print(f"{name} earned {earning}$ this week.")