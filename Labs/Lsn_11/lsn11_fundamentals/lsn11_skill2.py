from cs110 import autograder
import random

# ---------------------------------------------------------------------
# Lab: Lesson 11 - Fundamental Skill #2
# Course: CS110
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# PROBLEM STATEMENT:
# You are being provided with a list containing 5 random numbers.  Create
# a variable called my_value, and assign it the value of the 3rd item in
# the list.
# ---------------------------------------------------------------------

# This function creates a list with 5 random numbers.  Don't mess with it!
def create_random_list():
    result = []
    for i in range(5):
        result.append(random.randint(0, 100))
    return result

# This creates a list called my_list
my_list = create_random_list()

# Write the code needed to save the 3rd item in the list into the my_value variable
