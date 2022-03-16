from cs110 import autograder

# ---------------------------------------------------------------------
# Lab: Lesson 9 - Fundamental Skill #2
# Course: CS110
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# PROBLEM STATEMENT:
# You have been provided with a function called draw_multiple_trees()
# that outputs a tree using ASCII art.  Unlike the previous problem,
# this function accepts a parameter that tells it how many trees to draw.
#
# Write a program that:
# 1.  Gets an integer from the user and stores it in a variable.  You can name this variable whatever you want.
# 2.  Calls the function, and passes the variable to it.  
# ---------------------------------------------------------------------

# DO NOT TOUCH THIS FUNCTION
def draw_multiple_trees(num_trees_to_draw):
    for i in range(num_trees_to_draw):
        print("  *  ")
        print(" *** ")
        print("*****")
        print("  |  ")


# Write Your Code Here
