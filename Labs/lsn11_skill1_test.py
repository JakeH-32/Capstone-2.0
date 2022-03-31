from cs110 import autograder
import random
from lsn11_skill1 import *

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    if 'my_list' in globals():
        print("Looking for my_list . . . FOUND!")
        if len(my_list) == 3:
            print("Looking inside my_list . . . FOUND 3 ITEMS!")
            return 100
        else:
            print("Looking inside my_list . . . FOUND", len(my_list), "INSTEAD OF 3 ITEMS")
            return 50
    else:
        print("Looking for my_list . . . NOT FOUND!")
        return0
        
        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)
