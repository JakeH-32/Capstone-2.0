from cs110 import autograder
import random, math

# The Actual Solution
def draw_tree():
    result =  "  *  \n"
    result += " *** \n"
    result += "*****\n"
    result += "  |  \n"
    return result;


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    output, error_message = autograder.run_script("lsn9_skill1.py", [])
    
    expected_output = draw_tree() + draw_tree () + draw_tree()
    
    if output == expected_output:
        print("Good Job!")
        return 100
    else:
        print("Incorrect Output. Expected the following:")
        print(expected_output)
    
    return 0

        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)