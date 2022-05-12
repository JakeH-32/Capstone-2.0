from cs110 import autograder

# ---------------------------------------------------------------------
# Lab: Lesson 11 - Call Me...Maybe
# Course: CS110, Spring 2021
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# PROBLEM STATEMENT:
# You have been provided with three functions.  Complete the tasks described
# below and call these functions as needed.
# ---------------------------------------------------------------------

# This function calculates the area of a rectangle, given its height and width
def area_rectangle(width, height):
    print(width * height)

# This function takes a string and prints it backwards
def print_backwards(string_to_print):
    for i in range(len(string_to_print)-1, -1, -1):
        print(string_to_print[i], end='')
    print()

# This function takes a number and determines if it is Negative, Positive, or Zero
def positive_or_negative(value):
    if value > 0:
        print("Positive")
    elif value < 0:
        print("Negative")
    else:
        print("Zero")


# Task 1:  Ask the user to enter a width and height.  Do NOT  assume they are whole numbers. Call area_rectangle and give it the user values


# Task 2:  Ask the user to enter a string.  Call print_backwards and give it the user value

my_number = 2024
# Task 3:  You have been provided with a variable called my_number.  Call positive_or_negative and give it the variable

