## 1. Convert the loop into a list comprehension:
number = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in number]

## 2. Sử dụng comprehension tạo 1 từ điển mới
movie = {
    "title": "thor: ragnarok",
    "director": "taika waititi",
    "producer": "kevin feige",
    "production_company": "marvel studios"
}
movie = {key: value.title() for key, value in movie.items()}
print(squares)
print(movie)

