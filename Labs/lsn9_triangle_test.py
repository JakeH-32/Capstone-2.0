from cs110 import autograder
import random, math
import lsn9_triangle

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    base = round(random.uniform(1.0, 10.0), 1)
    height = round(random.uniform(1.0, 10.0), 1)
    output, error_message = autograder.run_script("lsn9_triangle.py", [base, height])
    
    area = (base * height) / 2.0
    score = 0
    
    if "area_triangle" in dir(lsn9_triangle):
        print("Function Correctly Defined")
        score += 50
    else:
        print("Function does not exist.  Check to make sure the name matches the prompt")
    
    if autograder.equals(output, area):
        print("Function produces correct output")
        score += 50
    else:
        print("Function produces incorrect output. Expected:", area)
    
    return score

        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)