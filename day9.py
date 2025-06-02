## Unpacking, Enumeration, the zip function
#Unpack
movies = [("The Matrix", 1999, "Sci-Fi")
          , ("The Godfather", 1972, "Crime")
          , ("Pulp Fiction", 1994, "Crime")]
#Thay vì : title = movie[0]
#     year = movie[1]
#     genre = movie[2]
title, year, genre = movies
for title, year, genre in movies:
    print(f"{title} was released in {year} and is a {genre} movie.")

# Enumate
# for index in range(len(movies)):
#     print (f"{index +1}. {movies[index][0]}({movies[index][2]}), by {movies[index][1]}")
#Cách khác
# counter = 1

# for title, year, genre in movies:
#     print(f"{counter}. {title}({genre}), by {year}")
#     counter += 1

for counter, movies in enumerate(movies, start=1):
    print(f"{counter}. {movies[0]}({movies[2]}), by {movies[1]}")

# #Zip
pet_owners = ["Alice", "Bob", "Charlie"]
pet_names = ["Fluffy", "Fido", "Whiskers"]
pet_ages = [3, 5, 2]
pets_and_owners = list(zip(pet_owners, pet_names, pet_ages))
print(pets_and_owners)
