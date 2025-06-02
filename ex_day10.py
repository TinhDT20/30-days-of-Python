album = {
    "title": "The Dark Side of the Moon",
    "artist": "Pink Floyd",
    "year": 1973,
    "tracks": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]
}
#  Iterate over the keys and values of the dictionary
for key in album:
    print(f"{key}: {album[key]}")
del album["tracks"]
del album["year"]
album["date"] = "March 1, 1973"
print(album.get("year")) # None
print(album.get("date")) # March 1, 1973