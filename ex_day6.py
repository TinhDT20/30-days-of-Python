employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
# In ra số tiền được nhận cuối tuần của mỗi ngườingười
for i in employees:
    print(f"{i[0]} is due to be paid at the end of the week is ${i[1]*i[2]}")
count = 0
total = 0
for i in employees:
    count = count + 1
    total = total + i[2]

average = total / count
print(average)

name = []
for i in employees:
    if i[2] > average:
        name.append(i[0])
print(f"{', '.join(name)} have wage higher than average wage ")
