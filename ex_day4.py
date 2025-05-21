movies = [
    ("Lilo & Stitch", "Chris Sanders & Dean DeBlois", 2002, "$80 milions USD" ),
    ("The Lion King", "Roger Allers & Rob Minkoff", 1994, "$763.5 milions USD"),
    ("The Incredibles", "Brad Bird", 2004, "$631.4 milions USD")
]
title = input ("Please enter the movie name, : ")
director = input ("Please enter the director name, : ")
year = int(input ("Please enter the year, : "))
budget = input ("Please enter the budget, : ")

print(f"Movie {title} was directed by {director} in {year} with a budget of {budget}.")

add_movie = (title, director, year, budget)
movies.append(add_movie)
print(movies)

for i in range(len(movies)):
    print(f"Movie {i+1}: {movies[i][0]} was directed by {movies[i][1]} in {movies[i][2]} with a budget of {movies[i][3]}.")

del movies[0]