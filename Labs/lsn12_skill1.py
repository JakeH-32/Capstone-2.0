from cs110 import autograder

# ---------------------------------------------------------------------
# Lab: Lesson 12 - Fundamental Skill #1
# Course: CS110, Fall 2020
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# PROBLEM STATEMENT:
# You have been provided with a function called get_fuel_consumption()
# that takes a distance in kilometers as a parameter, and calculates the
# fuel consumed (in gallons) by a 747 aircraft to travel this distance.
#
# Use this function to determine how much fuel is consumed by a 747 when
# traveling 1500 kilometers.  Store the returned result in a variable
# called fuel_consumed
# ---------------------------------------------------------------------

# DO NOT TOUCH THIS FUNCTION
def get_fuel_consumption(distance_in_kilometers):
    distance_in_miles = distance_in_kilometers * 0.621
    return 5 * distance_in_miles
    
# Your Code Goes Here



