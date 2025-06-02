# Comprehensions
# thay vì thêm 1 biến mới để xử lí thì có thể tái sử dungj lại biên đã có
# Ví dụ xử listist
name = ["mary", "Richard", "John", "KATE"]
age = [20, 30, 40, 50]

people = [(name.title(), age) 
            for name, age in zip(name, age)]

student_ids = (111, 222, 333, 444)
names = ["mary", "Richard", "John", "KATE"]
students = {student_id: name.title() 
            for student_id, name in zip(student_ids, names)}

print(people)
print(students)

