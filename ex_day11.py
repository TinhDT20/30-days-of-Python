empty_set = set()
empty_set.update(["cat","Tom","blue"])
set_1st = empty_set
print(set_1st)
set_2nd = {"cat","Mi","white"}
# hợp
union_set = set_1st.union(set_2nd)
# hiệu đối xứng
symmetric_difference_set1 = set_1st.symmetric_difference(set_2nd)
symmetric_difference_set2 = set_2nd.symmetric_difference(set_1st)

# giao
intersection_set = set_1st.intersection(set_2nd)
print(union_set)
print(symmetric_difference_set1)
print(symmetric_difference_set2)
print(intersection_set)
# {'blue', 'Tom', 'cat'}
# {'blue', 'Tom', 'Mi', 'white', 'cat'}
# {'Tom', 'blue', 'Mi', 'white'}
# {'blue', 'Tom', 'Mi', 'white'}
# {'cat'}
set_number = range(1,100,1)
number = int(input("please enter your number: "))
if number in set_number:
    print("Your number is in my set")
else:
    if number < set_number[0]:
        print("Your number is lower than all numbers in my set")
    else: 
        print("Your number is higher than all numbers in my set")