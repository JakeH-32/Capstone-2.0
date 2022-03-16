from cs110 import autograder

# ---------------------------------------------------------------------
# Lab: Get Movies
# Course: CS110
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Problem Statement:  Write a Python function called get_movies that takes three parameters:
#     - A two-dimensional array containing a list of movie titles and other stats (see table below for an example)
#     - A rating (e.g., "PG", "R")
#     - A run time (in minutes)
# Your function should return the number of movies that have the specified rating, and run for at least the number of minutes specified.
# ---------------------------------------------------------------------

# YOUR FUNCTION GOES HERE


# Here is an example list of movies to help you test your function
example_movies_table = [
        ["Star Wars: A New Hope", 1977, "PG", 121],
        ["Star Trek: The Motion Picture", 1979, "G", 132],
        ["Raiders of the Lost Ark", 1989, "PG", 115]]

# Here is a function call to help you test your function
print(get_movies(example_movies_table, "PG", 100))