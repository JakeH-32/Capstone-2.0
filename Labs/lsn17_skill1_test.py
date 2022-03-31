from cs110 import autograder
import random, math

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    score = 0.0
    
    if autograder.code_compiles("lsn17_skill1.py"):
        file = open("lsn17_skill1.py", "r")
        file_contents = file.read()
        
        if "draw_circle(" in file_contents:
            print("draw_circle called")
            score += 50
        else:
            print("draw_circle does not appear to be called.  You need to call it in the draw() function")
            
        if file_contents.count("ball_x") + file_contents.count("ball_y") > 5:
            print("Looks like you are using ball_x and/or ball_y")
            score += 50
        else:
            print("Make sure you are changing the value of ball_x and ball_y in update().")
            
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