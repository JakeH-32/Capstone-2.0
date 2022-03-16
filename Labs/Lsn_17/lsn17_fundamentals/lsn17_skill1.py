from cs110 import autograder
import pythonGraph

# ---------------------------------------------------------------------
# Lab: Lesson 17 - Graphics II - Fundamental Skill #1
# Course: CS110
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# PROBLEM STATEMENT:
# You have been provided with the template code for an animation.
# Study the code for a minute, then perform the following tasks:
#    1.  In the draw() function, add one line of code that draws a circle.
#        For the center, use the ball_x and ball_y variables defined below.
#    2.  In the update() function, add code that modifies these variables.
#        For example, add 1 to the ball's x-coordinate and subtract 1 from
#        the ball's y-coordinate every time update() is called.
#        What do you expect to happen?
#        Does what actually happens match your expectations?
# ---------------------------------------------------------------------

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Lsn 17 - Moving Ball Demo"

# Setup Tasks for the Window
pythonGraph.open_window(WINDOW_WIDTH, WINDOW_HEIGHT)
pythonGraph.set_window_title(WINDOW_TITLE)

# Initialize Graphics Variables
ball_x = 300
ball_y = 300

# Animation Functions
def erase():
    pythonGraph.clear_window("WHITE")

def draw():
    # "pass" is a magical word in Python that tells it to do nothing
    # We include it in this function because every functions must have at least one line of code
    pass

def update():
    # This line is semi-magical; it tells python that we want to modify the ball x and y variables above
    # We will talk more about this in class
    global ball_x, ball_y   

# Animation Loop
# DO NOT TOUCH!
while pythonGraph.window_not_closed():
    
    # Erase Everything
    erase()
    
    # Draw the ball
    draw()
    
    # Update the ball's location
    update()
    
    # Shows All Drawings Above
    pythonGraph.update_window()




