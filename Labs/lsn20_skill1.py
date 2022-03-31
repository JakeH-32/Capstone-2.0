from cs110 import autograder

# ---------------------------------------------------------------------
# Lab: Lesson 20 - Fundamental Skill #1
# Course: CS110, Fall 2020
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# PROBLEM STATEMENT:
# You have been provided with code that opens a CSV file.  Refer to the writeup to see what the file contains.
#
# Do the following:
# Line 30:  Write a line of code that extracts the columns from each line.  Use the split() function
# Line 33:  Create a new row (i.e., a list) that contains the number of silver medals, followed by the name of the country
# Line 36:  Append the new row to my_table
# ---------------------------------------------------------------------

# Opens the file, and gets each line of text
file = open("olympics.csv", "r")
file_contents = file.read()
lines_in_file = file_contents.split('\n')

# Creates an empty table
my_table = []

# Loops Through Every line in the File
for line in lines_in_file:
    
    # Write a line of code that extracts the columns from each line.  Use the split() function
    
    
    # Create a new row (i.e., a list) that contains the number of silver medals, followed by the name of the country
    
    
    # Append the new row to my_table
    
    