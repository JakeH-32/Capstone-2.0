from cs110 import autograder
import pythonGraph, random

# ---------------------------------------------------------------------
# Lab - Graphics II: Bouncing Triangle
# Course: CS110
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Problem Statement: Create an animation of a bouncing triangle.
# ---------------------------------------------------------------------

# Setup Tasks for the Window
pythonGraph.open_window(600, 600)
pythonGraph.set_window_title("Bouncing Triangle")

# Initialize Graphics Variables
p1_x = random.randint(0, 600)
p1_y = random.randint(0, 600)
p1_vx = random.random() * 3.0
p1_vy = random.random() * 3.0

p2_x = random.randint(0, 600)
p2_y = random.randint(0, 600)
p2_vx = random.random() * 3.0
p2_vy = random.random() * 3.0

p3_x = random.randint(0, 600)
p3_y = random.randint(0, 600)
p3_vx = random.random() * 3.0
p3_vy = random.random() * 3.0

def erase():
    pass

def draw():
    pass

def update():
    pass


# Animation Loop
while pythonGraph.window_not_closed():
    
    # Erase Everything
    erase()
    
    # Draw
    draw()
    
    # Update
    update()
    
    # Shows All Drawings Above
    pythonGraph.update_window()

