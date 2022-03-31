from cs110 import autograder
import random, math


def get_value(n):
    return (2 * n) + 1


def solution(x):
    result = ''
    
    for i in range(x, x+6):
        result += str(get_value(i)) + "\n"
    
    return result


def test_passed():
    random_value = random.randint(5, 15)
    output, error = autograder.run_script("PA2_practice2.py", [random_value])
    expected_output = solution(random_value)
    
    if output.strip() == expected_output.strip():
        print("CORRECT")
        return 100.0
    else:
        print("INCORRECT.  Expected:")
        print(expected_output)
    
    return 0.0
    
        
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