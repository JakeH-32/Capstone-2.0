from cs110 import autograder

# ---------------------------------------------------------------------
# Lab: Simple Drawing
# Course: CS110
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Problem Statement:   Using pythonGraph (and the documentation for pythonGraph),
# experiment with each of the drawing commands listed (drawing commands begin with the keyword "draw").
# Draw something interesting using at least 4 different drawing commands.
# One of those drawing commands must be an image
# ---------------------------------------------------------------------
import pythonGraph

SCREEN_TITLE = "Lesson 18: Simple Drawing"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Setup tasks for window
pythonGraph.open_window(SCREEN_WIDTH, SCREEN_HEIGHT)
pythonGraph.set_window_title(SCREEN_TITLE)

# DRAWING goes here
pythonGraph.write_text("Hello World!", 5, 5, pythonGraph.colors.BLACK)

# Wait using the window is closed
pythonGraph.wait_for_close()