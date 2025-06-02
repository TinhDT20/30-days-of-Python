# Sets: Tập hợp
vegetables = {"carrot", "lettuce", "broccoli", "onion", "carrot"}
# là giống với vegetables = {"carrot", "lettuce", "broccoli", "onion"}
# # không có thứ tự, không có chỉ số, không thể truy cập bằng chỉ số
# tập rỗng set()
empty_set = set()
# điều này là không hợp lệ nested_sets = {{1,  2,  3},  {"a",  "b",  "c"}}
# thêm mục = add
vegetables.add("potato")
# thêm nhiều mục = update
vegetables.update(["pumpkin", "zucchini"])
print(vegetables)
# xó random dùng pop
random_vegetable = vegetables.pop()
print(vegetables)
# clear để làm rỗng tập
# hợp các tập hợp
letters = {"a","b","c"}
numbers = {1, 2, 3}
letters_and_numbers = letters.union(numbers)
print(letters_and_numbers)
# union tạo ra tập mới, update sửa tâp cũ
# giao 2 tập hợp
mod_2 = {2, 4, 6, 8, 10, 12, 14, 16, 18}
mod_3 = {3, 6, 9, 12, 15, 18}
mod_6 = mod_2.intersection(mod_3)
print(mod_6)  # {18, 12, 6}
# different
bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}
print(bundle_1.difference(bundle_2))  # {'Final Fantasy VII', 'Cyberpunk 2077'}
print(bundle_2.difference(bundle_1))  # {'Halo Infinite', 'Doom Eternal'}
# symmetric_difference
bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}

print(bundle_1.symmetric_difference(bundle_2))

# {'Cyberpunk 2077', 'Final Fanstay VII', 'Halo Infinite', 'Doom Eternal'}
#Kiểm tra xem các mục có trong bộ sưu tập không
print(3 in numbers)  # True
print(7 in numbers)  # False
