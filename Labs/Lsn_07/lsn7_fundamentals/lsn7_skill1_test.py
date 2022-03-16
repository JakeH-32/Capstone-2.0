from cs110 import autograder
import random, math

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    score = 0.0
    
    if autograder.code_compiles("lsn7_skill1.py"):
        file = open("lsn7_skill1.py", "r")
        file_contents = file.read()
    
        print("----------------------------------------------------------------------")
        print("*** To Actually See Your Graphics, Rerun this Program and Type 'N' ***")
        print("----------------------------------------------------------------------\n")
    
        if "open_window(" in file_contents:
            print("open_window Called")
            score += 33
        else:
            print("open_window does not appear to be called")
        
        if "draw_circle(" in file_contents:
            print("draw_circle Called")
            score += 34
        else:
            print("draw_circle does not appear to be called")
            
        if "wait_for_close(" in file_contents:
            print("wait_for_close Called")
            score += 33
        else:
            print("wait_for_close does not appear to be called")
            
    else:
        print("There appears to be an error in your python Script that is preventing it from running")
    
    return score        
    
        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result) 