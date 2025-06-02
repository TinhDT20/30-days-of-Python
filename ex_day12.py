#Ex1
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b 
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        print("Cannot divide by zero")
    else:       
        return a / b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Tổng 2 số là: {add(a,b)}")
print(f"Hiệu 2 số là: {subtract(a,b)}")
print(f"Nhân 2 số là: {multiply(a,b)}")
print(f"Chia 2 số là: {divide(a,b)}")
#Ex2
def print_show_info(show):
    print(f"{show['title']} ({show['initial_release']}) - {show['seasons']} seasons ")
tv_shows = {
    "title": "Breaking Bad",
    "initial_release": 2008,
    "seasons": 5
}
print_show_info(tv_shows)
# Ex3
series = [
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016}
]

for show in series:
    print_show_info(show)

#Ex4
def check_palindrome(word):
    word = word.lower().strip()
    if word == word[::-1]:
        print(True)
    else:
        print(False)
word = input("Enter a word: ")
check_palindrome(word)
