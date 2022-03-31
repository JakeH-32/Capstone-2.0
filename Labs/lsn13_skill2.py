from cs110 import autograder

# ---------------------------------------------------------------------
# Lab: Lesson 13 - Fundamental Skill #2
# Course: CS110
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# PROBLEM STATEMENT:
# You are trying to use a for loop to print all of the powers of 2 from
# 1024 (2^10) to 1 (2^0).  Unfortunately, for some reason, the loop
# does not work.  Review the code and make the ncessary corrections.
# ---------------------------------------------------------------------

# HINT:  When using range()
#     - the first number is the starting number
#     - the second number is the ending number
#     - the last number is the amount to change i by after each iteration

# This loop is broken.  Fix it!
for i in range(10, 1, -1):
    print(2**i)
