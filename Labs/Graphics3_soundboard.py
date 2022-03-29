from cs110 import autograder
import pythonGraph

# ---------------------------------------------------------------------
# Lab: pythonGraph Soundboard
# Course: CS110
# ---------------------------------------------------------------------

# Setup Tasks for the Window
pythonGraph.open_window(500, 350)
pythonGraph.set_window_title("Soundboard")

# Animation Loop
while pythonGraph.window_not_closed():
    
    # Gets the Mouse Coordinates
    mouse_x = pythonGraph.get_mouse_x()
    mouse_y = pythonGraph.get_mouse_y()
    pythonGraph.set_window_title("Soundboard (x:" + str(mouse_x) + ", y:" + str(mouse_y) + ")")
    
    # Draw Button 1
    pythonGraph.draw_rectangle(50, 50, 150, 150, pythonGraph.colors.RED, True)
    pythonGraph.draw_text("Sound 1", 60, 90, pythonGraph.colors.WHITE)
    
    # Draw Button 2


    # Draw Button 3


    # Draw Button 4

    
    # Draw Button 5


    # Draw Button 6


    # Check for Mouse Presses Here
    if pythonGraph.mouse_button_pressed(pythonGraph.mouse_buttons.LEFT):

        # Checks to see if we are in the coordinates of Button 1
        if mouse_x >= 50 and mouse_x <= 150 and mouse_y > 50 and mouse_y < 150:
            pythonGraph.play_sound_effect("sound1.wav")
    
    # Shows All Drawings Above
    pythonGraph.update_window()


