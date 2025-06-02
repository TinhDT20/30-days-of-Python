# # #EX1
# # def exponentiate (base, exponent):
# #     return base ** exponent
# # print(exponentiate(2, 3))
# #ex2
# def process_string(string):
#     string = string.strip().lower()
#     return string
# string = input("Enter a string: ")
# print(process_string(string))
# #ex3
# def get_info(actor):
#     name = actor.get("name")
#     nationality = actor.get("nationality")
#     age = actor.get("age")
#     return ({name}, {nationality}, {age})
# actor  = {"name": "Tom Hardy", "nationality": "English", "age": 42}

# print(get_info(actor))
#ex4
def is_prime(n):
    if n < 2: 
        return False
    else:
        count = 0
        for i in range(2,n):
            if n % i == 0:
                count += 1
                break
        if count == 0:
            return True
        else:
            return False

n = int(input("Enter a number: "))
print(is_prime(n))