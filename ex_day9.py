main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for name, voice, species in main_characters:
    print(f"{name} is a {species.lower()} voiced by {voice}.")

# Ex2
data = ("John Smith", 11743, ("Computer Science", "Mathematics"))
name, id, (majors, minor) = data

#Ex3 Nén 2 tệp có độ dài khác nhau 
name_student = ["Tom", "Jerry", "Spike", "Tyke"]
id_student = [1, 2, 3, 4, 5]

print(list(zip(name_student, id_student))) #[('Tom', 1), ('Jerry', 2), ('Spike', 3), ('Tyke', 4)]