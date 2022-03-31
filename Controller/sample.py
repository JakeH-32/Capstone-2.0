from cs110 import autograder

# ---------------------------------------------------------------------
# Sample Student Code
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Problem Statement:  Write an algorithm that first asks the user how many
# cadets to input and then gets that many cadet class years from the user.
# Output how many of those cadets were in the class of 2017. 
# ---------------------------------------------------------------------

# Ask how many cadets there will be
cadets = int(input())

# Set the count to 0, just in case there are none
count = 0

# Loop through the cadets and ask their class year.

# Using a While Loop
i = 0  # Counts the number of times we have been through the loop

while i < cadets:
    year = int(input())
    if (year == 2017):
        count = count + 1
    i = i + 1

print(count)