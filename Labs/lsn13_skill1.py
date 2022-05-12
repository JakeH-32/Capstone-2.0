from cs110 import autograder

# ---------------------------------------------------------------------
# Lab: Lesson 13 - Fundamental Skill #1
# Course: CS110, Fall 2020
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# PROBLEM STATEMENT:
# You have been provided with a WHILE loop that prints the values from
# 0 to 10.  Modify this loop so that it counts by 2s instead of 1s
# ---------------------------------------------------------------------

# ITEM is an acronym that we use to help us remember the components of
# a WHILE loop

# I:  Initialize Loop Control Variable
# The loop control variable is used to determine when we are done with the loop.
# We can name it whatever we want
i = 0

# T:  Test
# This is where we look at the loop control variable and decide if we are done
# The loop will continue for as long as the test is TRUE
while i <= 10:

    # E:  Execute
    # This is where we do the thing we want to do multiple times
    print(i)

    # M:  Modify Loop Control Variable
    # This is where we change the value of the loop control variable
    # if we do not do this, the loop will never end
    i = i + 1

