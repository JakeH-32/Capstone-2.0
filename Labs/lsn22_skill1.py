from cs110 import autograder
import pythonGraph

# ---------------------------------------------------------------------
# Lab: Lesson 22 - Fundamental Skill #1
# Course: CS110, Fall 2020
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# PROBLEM STATEMENT:
# You have been provided with the template code for an animation.
# Study the code for a minute, then perform the following tasks:
#    1.  In the draw() function, add one line of code that draws a circle.
#        For the center, use the variables defined on lines 23 and 24
#    2.  In the update() function, add code that modifies the variables on lines 23 and 24.
#        For example, add 1 to ball's x-coordinate every time update() is called, and see what happens.
# ---------------------------------------------------------------------

# Setup Tasks for the Window
pythonGraph.open_window(600, 600)
pythonGraph.set_window_title("Lsn 22 - Moving Ball Demo")

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




