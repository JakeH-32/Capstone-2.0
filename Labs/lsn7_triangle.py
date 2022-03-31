from cs110 import autograder
import pythonGraph

# ---------------------------------------------------------------------
# Lab: Triangle
# Course: CS110
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Problem Statement:   Write an algorithm that asks the user for X and Y
# coordinates of a single point (the coordinates of the top left point on the triangle),
# the length of the base, and the height of a right triangle.
# Then, open a graphics window and draw the triangle.
# ---------------------------------------------------------------------
SCREEN_TITLE = "Lesson 18: Triangle"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Setup tasks for window
pythonGraph.open_window(SCREEN_WIDTH, SCREEN_HEIGHT)
pythonGraph.set_window_title(SCREEN_TITLE)

# DRAWING goes here
pythonGraph.write_text("Hello World!", 5, 5, pythonGraph.colors.BLACK)

# Wait using the window is closed
pythonGraph.wait_for_close()
