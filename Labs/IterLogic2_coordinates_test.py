from cs110 import autograder
import random, math

def solution(start_x, end_x, start_y, end_y):
    result = ''

    for y in range(start_y, end_y+1):
        for x in range(start_x, end_x+1):
            result += str(x) + " " + str(y) + "\n"

    return result


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    start_x = random.randint(-2, -1)
    end_x = random.randint(1, 2)
    start_y = random.randint(-3, -1)
    end_y = random.randint(1, 3)

    output, error_message = autograder.run_script("IterLogic2_coordinates.py", [start_x, end_x, start_y, end_y])
    expected_output = solution(start_x, end_x, start_y, end_y)
    
    lines = output.strip().split('\n')
    num_matches = autograder.compare_strings(lines, expected_output.strip().split('\n'))

    return 100 * (num_matches / len(lines))

        
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