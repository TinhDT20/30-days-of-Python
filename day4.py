# Basic Python Collections
# 1. List 
# # Dùng [] để tạo danh sách, có thể trộn bấy kỳ loại giá trị nào với nhau
movie_title = [
    "Doraemon",
    "Lilo & Stitch",
    "The Lion King",
    "The Little Mermaid",
    "The Incredibles",
    "Finding Nemo"
]
# # Truy cập giá trị
print(movie_title[0]) # Doraemon
print(movie_title[-1]) # Finding Nemo
# # Thêm mục vào danh sách
a = movie_title
movie_title.append("Frozen")
print(movie_title, a)
movie_title = movie_title + ["Frozen"]
print(movie_title, a)
# # Sự khác nhau của toán tử + và phương thức append() là:
# # - Toán tử + tạo ra một danh sách mới, trong khi append() thêm phần tử vào danh sách hiện tại. 
# # - Sử dụng + sẽ không thay đổi danh sách gốc a giống với movie_title cũ còn movie_title đã bị thay đổi , trong khi append() sẽ thay đổi danh sách gốc: movie_title thay đổi thì a cũng thay đổi.
# # insert
movie_title.insert(0, "Frozen")
print(movie_title)

# remove
movie_title.remove("Frozen") # Chỉ xóa phần tử đầu tiên
print(movie_title)
## del
del movie_title[0] # Xóa phần tử đầu tiên
print(movie_title)
## pop: mặc định xóa phần tử cuối, nhưng pop(1) cũng xóa phần tử thứ 2
movie_title.pop() # Xóa phần tử cuối 
##clear
movie_title.clear() # Xóa tất cả phần tử
print(movie_title)

# # 2. Tuple
# # Dùng () để tạo tuple, không thể thay đổi giá trị trong tuple
movie = [
    ("Doraemon", 1990),
    ("Lilo & Stitch", 2002)
]
# # Truy cập giá trị
print(movie[0][0]) # Doraemon
print(movie[0]) # ('Doraemon', 1990)