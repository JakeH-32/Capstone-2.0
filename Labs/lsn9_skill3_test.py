from cs110 import autograder
import random, math
import lsn9_skill3

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    output, error = autograder.run_script("lsn9_skill3.py", [])
    score = 0
    
    if "print_hello" in dir(lsn9_skill3):
        print("Function found!")
        score += 50
        
        if len(output) > 0:
            print("Output Found!")
            score += 50
        else:
            print("Function does not appear to be printing out anything")
    else:
        print("Function does not appear to be defined.  Check the name and make sure it matches the prompt")
    
    return score

        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)