from cs110 import autograder
import random, math

def solution(multiple):
    result = ''
    i = 1
    
    while i <= 10:
        result += str(i * multiple) + "\n"
        i += 1
    
    return result


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    random_multiple = random.randint(1, 20)

    output, error_message = autograder.run_script("IterLogic2_timestable.py", [random_multiple])
    expected_output = solution(random_multiple)
    
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