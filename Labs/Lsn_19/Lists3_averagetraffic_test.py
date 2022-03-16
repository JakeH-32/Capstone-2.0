from cs110 import autograder
import random, math

expected_output = ["525"]


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    output, error = autograder.run_script("Lists3_averagetraffic.py", [])
    lines = output.strip().split('\n')
    
    num_matches = autograder.compare_strings(lines, expected_output)
       
    return round(num_matches * (100.0 / len(expected_output)), 1)

        
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