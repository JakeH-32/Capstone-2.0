from cs110 import autograder
import random, math


def test_passed():

    num_tests_passed = 0
    test_cases = [("Regular", 37, 2.938), ("Midgrade", 37, 3.098), ("Premium", 37, 3.208), ("Diesel", 32, 3.242)]

    for test_case in test_cases:
        print("# -----------------------------------")
        print("# Testing", test_case[0])
        print("# -----------------------------------")
        output, error = autograder.run_script("PA2_practice4.py", [test_case[0]])
    
        lines = output.strip().split('\n')
        
        if len(lines) > 0:
            if autograder.equals(lines[0], test_case[2]):
                print("CORRECT")
                num_tests_passed += 1
            elif len(lines) > 1 and autograder.equals(lines[0], test_case[1]) and autograder.equals(lines[1], test_case[2]):
                print("CORRECT")
                num_tests_passed += 1
            else:
                print("INCORRECT")
            print()
                    
    return round(100 / len(test_cases), 1) * num_tests_passed
    
        
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