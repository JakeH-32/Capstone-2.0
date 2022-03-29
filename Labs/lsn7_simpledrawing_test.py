from cs110 import autograder
import random, math

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    drawing_functions = ["draw_arc", "draw_image", "draw_rectangle", "draw_circle", "draw_ellipse", "draw_line", "draw_pixel", "draw_text", "write_text"]
    drawing_functions_called = []
    
    print("----------------------------------------------------------------------")
    print("*** To Actually See Your Graphics, Rerun this Program and Type 'N' ***")
    print("----------------------------------------------------------------------\n")
    
    file = open("lsn7_simpledrawing.py", "r")
    file_contents = file.read()
    
    for f in drawing_functions:
        if f in file_contents and f not in drawing_functions_called:
            drawing_functions_called.append(f)
    
    if len(drawing_functions_called) >= 4 and "draw_image" in drawing_functions_called:
        print("Good Job!")
        return 100.0
    elif len(drawing_functions_called) >= 4 and "draw_image" not in drawing_functions_called:
        print("Missing at least one call of draw_image")
        return 90.0
    else:
        print("Not enough different drawing functions.  Need 4 unique (including draw_image) calls.")
        return 25 * len(drawing_functions_called)
    
        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)