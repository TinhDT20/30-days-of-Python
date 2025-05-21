movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
total = 0
count = 0
for i in movies:
    total += i[1]
    count += 1
average = total / count
print(f"Ngân sách trung bình của các bộ phim là {average}")

list = []
for i in movies:
    if i[1] > average:
        list.append(i[0])
print (f"các bộ phim có ngân sách cao hơn mức trung bình {', '.join(list)}")
print (f"vậy có tổng cộng là {len(list)} bộ phim có ngân sách cao hơn mức trung bình")