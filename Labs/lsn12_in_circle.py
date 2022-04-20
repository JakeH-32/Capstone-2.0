from cs110 import autograder
import math

# ---------------------------------------------------------------------
# Lab: Function - In Circle
# Course: CS110, Fall 2020
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# Problem Statement:  Write a function that determines if a point is within a circle.
# You will name your function in_circle. It has five parameters: the coordinates of
# the point that is to be tested as x1, y1 and the center of a circle given by a point,
# cir_x, cir_y and a radius, radius.
# ---------------------------------------------------------------------

def dist_point(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
