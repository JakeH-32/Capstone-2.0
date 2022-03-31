from cs110 import autograder
import random

from lsn3_skill1 import *

# Runs the Python script and sees if it passes the test(s)
def test_passed():
       
    points_earned = 0   
    
    print("Looking for a variable called 'name' . . . ", end='')
    
    if 'name' in globals():
        points_earned += 50
        print("FOUND!")
        print("Now, checking to make sure your name is a string")
        
        if type(name).__name__ == 'str':
            points_earned += 50
            print("Good Job", name + "!")
        else:
            print("Make sure you are surrounding your name with quotation marks")
    else:
        print("NOT FOUND :(")
        
    return points_earned


# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)