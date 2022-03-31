from cs110 import autograder
import random, math

def solution(value_to_count_to, increment):
    result = ''
    i = 10
    
    while i >= value_to_count_to:
        result += str(i) + "\n"
        i += increment
    
    return result

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    random_ending_number = 0
    random_increment = -1

    output, error_message = autograder.run_script("lsn12_skill2.py", [])
    expected_output = solution(random_ending_number, random_increment)
    
    lines = output.strip().split('\n')
    last_line = lines[len(lines)-1]

    if output.strip() == expected_output.strip():
        print("CORRECT")
        return 100
    else:
        print("INCORRECT.  Expected the following:")
        print(expected_output)
    
    return 0

        
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