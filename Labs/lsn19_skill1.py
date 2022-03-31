from cs110 import autograder

# ---------------------------------------------------------------------
# Lab: Lesson 19 - Fundamental Skill #1
# Course: CS110
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# PROBLEM STATEMENT:
# You have been provided with code that opens a CSV file.  Refer to the writeup to see what the file contains.
#
# Do the following:
# Line 31: Write a line of code to break up each line of text into columns. Hint: Use the split() function
# Line 35: Use the data from the previous step to create a new two-item list containing the number of silver medals, followed by the name of the country.
# Line 39: Append this two-item list to my_table
# ---------------------------------------------------------------------

# Opens the file, and gets each line of text
file = open("olympics.csv", "r")
file_contents = file.read()
lines_in_file = file_contents.split('\n')

# Creates an empty table
my_table = []

# Loops Through Every line in the File
for line in lines_in_file:
    
    # Write a line of code to break up each line of text into columns.
    # Hint: Use the split() function

    
    # Use the data from the previous step to create a new two-item list containing:
    #   The number of silver medals, followed by the name of the country


    
    # Append this two-item list to my_table
        