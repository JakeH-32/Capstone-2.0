from cs110 import autograder
import random, math

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    score = 0.0
    
    if autograder.code_compiles("lsn20_skill1.py"):
        file = open("lsn20_skill1.py", "r")
        file_contents = file.read()
        
        if "get_mouse_x(" in file_contents:
            print("get_mouse_x called")
            score += 33
        else:
            print("get_mouse_x does not appear to be called.")
            
        if "get_mouse_y(" in file_contents:
            print("get_mouse_y called")
            score += 33
        else:
            print("get_mouse_y does not appear to be called.")
            
        if "draw_circle(" in file_contents:
            print("draw_circle called")
            score += 34
        else:
            print("draw_circle does not appear to be called.")
            
    else:
        print("There appears to be an error in your python Script that is preventing it from running")
    
    print("\nThank you for your submission.  Your instructor will let you know if there is an issue.")
    return score        
    
        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)















# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------


# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------