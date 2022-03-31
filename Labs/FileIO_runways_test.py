from cs110 import autograder
import random, math

def solution(filename, length, width):
    file = open(filename, 'r')
    file_contents = file.read()
    lines_in_file = file_contents.split('\n')
    result = ''

    for line in lines_in_file:
        columns = line.split(',')
        if length <= float(columns[2]) and width <= float(columns[3]):
            result += columns[0] + "\n"

    file.close()
    
    return result


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    random_length = random.randint(3000, 4000)
    random_width = random.randint(100, 200)
    
    output, error_message = autograder.run_script("FileIO_runways.py", ["runways.csv", random_length, random_width])
    expected_output = solution("runways.csv", random_length, random_width)
    
    lines = output.strip().split('\n')
    expected_lines = expected_output.strip().split('\n')
    
    num_matches = autograder.compare_strings(lines, expected_lines)
    
    if num_matches == len(lines):
        print("CORRECT")
        return 100.0
    else:
        print("INCORRECT")
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