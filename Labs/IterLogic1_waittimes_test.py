from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    score = 0.0
    
    possible_tests = [[30, 45, 15, 5, 5, -999], [15, 30, 31, 29, 120, 90, -999]]
    possible_output = [[5, 1], [15, 3]]
    
    # Generates a Random Test
    random_index = random.randint(0, len(possible_tests)-1)
    random_test = possible_tests[random_index]
    expected_output = possible_output[random_index]
            
    output, error = autograder.run_script("IterLogic1_waittimes.py", random_test)
    
    lines = output.split('\n')
    
    if len(lines) > 0 and autograder.equals(lines[0], expected_output[0]):
        print("Min Wait Time is Correct")
        score += 50
    else:
        print("Min Wait Time is Incorrect.  Expected", expected_output[0])
        
    if len(lines) > 1 and autograder.equals(lines[1], expected_output[1]):
        print("Number of Lines With Over 30 Minute Wait Times is Correct")
        score += 50
    else:
        print("Number of Lines With Over 30 Minute Wait Times is Incorrect.  Expected", expected_output[1])
    
    return score


# Testbench (to be run on windows)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)




# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------


# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------