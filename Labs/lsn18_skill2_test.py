from cs110 import autograder
import random, math
from lsn18_skill2 import *

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    score = 0
    
    if len(squadron_table) >= 2:
        print("Squadron Table has at least 2 things in them.  Let's see what's inside!")
        score += 20
        
        if (squadron_table[0][0] == "Dogs of War" and squadron_table[0][1] == 3):
            print("First Row Added Correctly")
            score += 40
        else:
            print("Something is wrong with the first row.  Make sure you are appending a list!")
        
        if (squadron_table[1][0] == "Wolverines" and squadron_table[1][1] == 19):
            print("Second Row Added Correctly")
            score += 40
        else:
            print("Something is wrong with the second row.  Make sure you are appending a list!")
    else:
        print("Squadron Table does not appear to have (at least) 2 rows")
        
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