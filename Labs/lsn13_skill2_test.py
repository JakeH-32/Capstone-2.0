from cs110 import autograder
import random, math

def solution():
    result = ''
    i = 10
    
    while i >= 0:
        result += str(2 ** i) + "\n"
        i -= 1
    
    return result


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    output, error_message = autograder.run_script("lsn13_skill2.py", [])
    expected_output = solution()
    
    lines = output.strip().split('\n')

    if output.strip() == expected_output.strip():
        print("CORRECT")
        return 100
    else:
        print("INCORRECT.  Expected the following:")
        print(expected_output)
    
    return 0

        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)
