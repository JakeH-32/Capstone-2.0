from cs110 import autograder
import pythonGraph

# ---------------------------------------------------------------------
# Lab: Stamp
# Course: CS110, Fall 2020
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Problem Statement: Create a pythonGraph function called draw_stamp that 
# accepts an x and y coordinate as parameters.  Your function will then 
# draw a picture (of your choosing) centered on that coordinate.
# ---------------------------------------------------------------------

SCREEN_TITLE = "Lesson 21: Stamp"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Draws whatever picture you want (centered on the x and y coordinate) 
def draw_stamp(x, y):
    pass


# Setup tasks for window
pythonGraph.open_window(SCREEN_WIDTH, SCREEN_HEIGHT)
pythonGraph.set_window_title(SCREEN_TITLE)

# DRAWING goes here
pythonGraph.write_text("Hello World!", 5, 5, pythonGraph.colors.BLACK)

# Test Code:  Feel Free to Change
draw_stamp(100, 100)
draw_stamp(500, 500)

# Wait using the window is closed
pythonGraph.wait_for_close()