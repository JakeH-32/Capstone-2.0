from cs110 import autograder
import random, math

def solution(start_char, end_char):
    result = ''
    
    start_char = ord(start_char)
    end_char = ord(end_char)
    
    if start_char < end_char:
        for i in range(start_char, end_char+1, 1):
            result += chr(i) + '\n'
    else:
        for i in range(start_char, end_char-1, -1):
            result += chr(i) + '\n'

    return result


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    score = 0
    
    print("# ------------------------------------------")
    print("# Test 1:  First letter lower than second")
    print("# ------------------------------------------")
    start_char = chr(random.randint(65, 85))
    end_char   = chr(random.randint(ord(start_char), 90))

    output, error_message = autograder.run_script("IterLogic2_printchars.py", [start_char, end_char])
    expected_output = solution(start_char, end_char)
    
    lines = output.strip().split('\n')
    last_line = lines[len(lines)-1]

    if output.strip() == expected_output.strip():
        print("CORRECT\n")
        score += 50
    else:
        print("INCORRECT.  Expected the following:")
        print(expected_output)
        
    
    print("# ------------------------------------------")
    print("# Test 2:  First letter higher than second")
    print("# ------------------------------------------")
    start_char = chr(random.randint(85, 90))
    end_char   = chr(random.randint(65, 84))

    output, error_message = autograder.run_script("lsn14_printchars.py", [start_char, end_char])
    expected_output = solution(start_char, end_char)
    
    lines = output.strip().split('\n')
    last_line = lines[len(lines)-1]

    if output.strip() == expected_output.strip():
        print("CORRECT\n")
        score += 50
    else:
        print("INCORRECT.  Expected the following:")
        print(expected_output)
    
    return score

        
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