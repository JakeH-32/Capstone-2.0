from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    score = 0.0
    
    possible_tests = [[8000, 12000, 25000, 10000, 7500, -1], [5000, 9000, 22000, 10000, 8700, -1], [9999, 5000, 3000, -1]]
    possible_output = [[7500, 25000, 3], [5000, 22000, 2], [3000, 9999, 0]]
    
    # Generates a Random Test
    random_index = random.randint(0, len(possible_tests)-1)
    random_test = possible_tests[random_index]
    expected_output = possible_output[random_index]
            
    output, error = autograder.run_script("IterLogic1_cargocapacity.py", random_test)
    
    lines = output.split('\n')
    
    if len(lines) > 0 and autograder.equals(lines[0], expected_output[0]):
        print("Min Value is Correct")
        score += 30
    else:
        print("Min Value is Incorrect.  Expected", expected_output[0])
    
    if len(lines) > 1 and autograder.equals(lines[1], expected_output[1]):
        print("Max Value is Correct")
        score += 30
    else:
        print("Max Value is Incorrect.  Expected", expected_output[1])
        
    if len(lines) > 2 and autograder.equals(lines[2], expected_output[2]):
        print("Number of Aircraft with At Least 10000 lbs is Correct")
        score += 40
    else:
        print("Number of Aircraft with At Least 10000 lbs is Incorrect.  Expected", expected_output[2])
    
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