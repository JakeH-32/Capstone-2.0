from cs110 import autograder
import random, math

def solution(filename, letter):
    result = ''
    
    file = open(filename, "r")
    contents = file.read()
    lines = contents.split("\n")

    for line in lines:
        if line[0] == letter:
            result += line + "\n"

    file.close()

    return result


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    random_letter = chr(random.randint(97, 122))
    
    output, error_message = autograder.run_script("FileIO_echo.py", ["file.txt", random_letter])
    expected_output = solution("file.txt", random_letter)
    
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