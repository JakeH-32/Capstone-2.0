import cs110, math

# ---------------------------------------------------------------------
# Assessment 1, Problem 5
# Course: CS110, Fall 2020
# ---------------------------------------------------------------------

# THIS CODE WORKS.  DO NOT TOUCH
vehicle_speed = float(input())

# YOUR CODE GOES HERE
if vehicle_speed <= 60 and vehicle_speed >= 50:
    print("Safe Speed")
else:
    print("Unsafe Speed")
