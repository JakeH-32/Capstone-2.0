from cs110 import autograder
import random, math

def solution(value_to_count_to, increment):
    result = ''
    i = 0
    
    while i <= value_to_count_to:
        result += str(i) + "\n"
        i += increment
    
    return result

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    random_ending_number = 10 + 2 * random.randint(1, 10)
    random_increment = 2

    output, error_message = autograder.run_script("IterLogic1_count.py", [random_ending_number, random_increment])
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

        
# Testbench (to run on outside of zyBooks)
if __name__ == '__main__':   
    result = test_passed()
    print("Unit Test Returned:", result)











# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------


# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------