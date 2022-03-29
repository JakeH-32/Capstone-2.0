from cs110 import autograder
import random, math
from lsn11_skill2 import *

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    if 'my_value' in globals():
        print("Looking for my_value . . . FOUND!")
        if my_value == my_list[2]:
            print("Looking inside my_value . . . VALUE MATCHES THE 3rd VALUE IN THE LIST")
            return 100
        elif my_value == my_list[3]:
            print("Looking inside my_value . . . VALUE MATCHES THE 4th VALUE INSTEAD OF THE THIRD!")
            print("** HINT:  The index starts at 0 **")
            return 50
        else:
            print("Looking inside my_value . . . VALUE DOES NOT MATCH.  EXPECTED", my_list[2])
            return 50
    else:
        print("Looking for my_value . . . NOT FOUND!")
        return 0
        
        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)

