from cs110 import autograder
import random, math

def solution(random_start, random_end, random_increment):
    result = ''

    for i in range(random_start, random_end+1, random_increment):
        result += str(i) + "\n"

    return result


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    random_start = random.randint(0, 10)
    random_end = random.randint(50, 100)
    random_increment = random.randint(2, 9)

    output, error_message = autograder.run_script("IterLogic2_counting.py", [random_start, random_end, random_increment])
    expected_output = solution(random_start, random_end, random_increment)
    
    lines = output.strip().split('\n')
    last_line = lines[len(lines)-1]

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


# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------


# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------