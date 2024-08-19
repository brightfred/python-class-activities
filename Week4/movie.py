import random  # Ensure random is imported

# Movies data
movies = {
    ("The Matrix", 1999),
    ("Lord of the Rings", 2010),  # Fixed capitalization and title
    ("The Godfather", 1972),
    ("Pulp Fiction", 1994),
    ("The Dark Knight", 2008),  # Changed to the correct movie title for 2008 Batman
    ("Fight Club", 1999),
    ("Forrest Gump", 1994),
    ("Schindler's List", 1993),  # Corrected spelling
    ("Gladiator", 2000),  # Fixed release year
    ("Jurassic Park", 1993)
}

# List comprehension for movies before 2000
movies_2000 = [title for title, year in movies if year < 2000]
print(movies_2000)  # Uncomment to display the result

# Dictionary comprehension for movies before 2000
movie_dict = {title: year for title, year in movies if year < 2000}
print(movie_dict)

# Verb, subject, adjective, and noun lists for random story generation
verb = ["go", "run", "jump", "walk", "swim", "fly", "drive", "sail", "ride", "climb"]
subject = ["I", "You", "He", "She", "It", "We", "They"]
adjective = ["big", "small", "tall", "short", "fat", "thin", "heavy", "light", "fast", "slow"]
noun = ["car", "bus", "train", "plane", "ship", "bicycle", "motorcycle", "boat", "rocket", "helicopter"]

# Generate and print a random story
story = [random.choice(subject) + " " + random.choice(verb) + " " + random.choice(adjective) + " " + random.choice(noun) for _ in range(5)]
print(story)





