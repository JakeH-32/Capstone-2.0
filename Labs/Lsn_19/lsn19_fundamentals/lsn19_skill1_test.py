from cs110 import autograder
import random, math
from lsn19_skill1 import *

answer= [[37, 'USA'],
        [23, 'Britain'],
        [18, 'China'],
        [17, 'Russia'],
        [10, 'Germany'],
        [8, 'Japan'],
        [18, 'France'],
        [3, 'South Korea'],
        [12, 'Italy'],
        [11, 'Australia']]

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    num_matches = 0
    count_vals_as_str = 0
    
    for i in range(len(my_table)):
        print("Row " + str(i+1) + ": ", end='')
        if i < len(answer):
            if my_table[i] == answer[i]:
                print("CORRECT")
                num_matches += 1
            else:
                if type(my_table[i][0]) is str:
                    count_vals_as_str += 1
                print("INCORRECT (Expected: " + str(answer[i]) + " instead of " + str(my_table[i]) + ")")
        else:
            print("INCORRECT (Unexpected Row: '" + str(my_table[i]) + "')")
    
    print()
    print(num_matches, "out of", len(answer), "rows match")
    if count_vals_as_str > 0:
        print("Looks like your medal numbers are strings not integers.")
    
    if len(answer) < num_matches:
        return 100 * num_matches / len(answer)
    else:
        return num_matches * (100 / len(answer))
    
    
        
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