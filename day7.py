# Day 7: split, join, and Slices
#join
list = ["apple", "banana", "cherry"]
print(f" My favorite fruit are {', '.join(list)}")
#  My favorite fruit are apple, banana, cherry
#split tách 1 chuỗi
string = "apple, banana, cherry"
list_fruit = string.split(", ")
print(list_fruit)
#slice
old_string = "0123456789"
slice_string = old_string[0:5]
print(slice_string) # 01234
#length: len
length = len(old_string)
print(length) # 10