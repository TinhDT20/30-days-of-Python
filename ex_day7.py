# # Bài 1: Yêu cầu người dùng nhập Họ tên, sau đó dùng split để tách ra, gán họ và tên cho 2 biến khác nhau
# name = input("Nhập họ tên của bạn: ").split()
# ## Họ tên sẽ được tách ra thành 2 biến là first_name và last_name
# first_name = name[0]       
# last_name = name[1]

# #Bài 2: 
# list = [1, 2, 3, 4, 5]
# processed_numbers = []
# for i in range(len(list)):
#     processed_numbers.append(str(i))
# print ((" | ".join(processed_numbers)))

#Bai 3:
quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]

for i in quotes:
    print(i.strip("'"))

# Bai 4:
sample_string = input("Please enter your sentence: ").strip()

character_count = len(sample_string)
word_count = len(sample_string.split())

print(f"Character count: {character_count}")
print(f"Word count: {word_count}")
