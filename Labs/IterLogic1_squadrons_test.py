from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    score = 0.0
    
    possible_tests = [[5, 10, 20, 30, 40, 19], [8, 3, 1, 23, 37, 40, 7, 6, 25]]
    possible_output = [[1, 2, 1, 1], [4, 0, 2, 2]]
    
    # Generates a Random Test
    random_index = random.randint(0, len(possible_tests)-1)
    random_test = possible_tests[random_index]
    expected_output = possible_output[random_index]
            
    output, error = autograder.run_script("IterLogic1_squadrons.py", random_test)
    
    lines = output.split('\n')
    
    if len(lines) > 0 and autograder.equals(lines[0], expected_output[0]):
        print("Num in Group One is Correct")
        score += 25
    else:
        print("Num in Group One is Incorrect.  Expected", expected_output[0])
        
    if len(lines) > 1 and autograder.equals(lines[1], expected_output[1]):
        print("Num in Group Two is Correct")
        score += 25
    else:
        print("Num in Group Two is Incorrect.  Expected", expected_output[1])
    
    if len(lines) > 2 and autograder.equals(lines[2], expected_output[2]):
        print("Num in Group Three is Correct")
        score += 25
    else:
        print("Num in Group Three is Incorrect.  Expected", expected_output[2])
    
    if len(lines) > 3 and autograder.equals(lines[3], expected_output[3]):
        print("Num in Group Four is Correct")
        score += 25
    else:
        print("Num in Group Four is Incorrect.  Expected", expected_output[3])
    
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