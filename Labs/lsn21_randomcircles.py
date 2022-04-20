from cs110 import autograder

# ---------------------------------------------------------------------
# Lab: Random Circles
# Course: CS110, Fall 2020
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Problem Statement: Create a pythonGraph that asks the user for the number 
# of circles to draw.  Your program should then open a pythonGraph window and 
# then draw that many circles somewhere within view.
# ---------------------------------------------------------------------
import pythonGraph, random

SCREEN_TITLE = "Lesson 20: Random Circles"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Setup tasks for window
pythonGraph.open_window(SCREEN_WIDTH, SCREEN_HEIGHT)
pythonGraph.set_window_title(SCREEN_TITLE)

# DRAWING goes here
pythonGraph.write_text("Hello World!", 5, 5, pythonGraph.colors.BLACK)

# Wait using the window is closed
pythonGraph.wait_for_close()