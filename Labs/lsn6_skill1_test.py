from cs110 import autograder
import random, math

num_tests_passed = 0
num_tests_run = 0

# The Actual Solution
def solution(body_temperature):
    if body_temperature >= 97 and body_temperature <= 99:
        return "Normal"
    else:
        return "Abnormal"


def run_test(body_temperature):
    global num_tests_run, num_tests_passed
    
    num_tests_run += 1
    
    print("--------------------------------------------")
    print("Testing Temperature =", body_temperature)
    print("--------------------------------------------")
    output, error_message = autograder.run_script("lsn6_skill1.py", [body_temperature])
        
    if output.strip() == solution(body_temperature):
        print("SUCCESS!\n")
        num_tests_passed += 1
    else:
        print("INCORRECT.  Expected:", solution(body_temperature), "\n")


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    run_test(96.9)
    run_test(97)
    run_test(98.5)
    run_test(99)
    run_test(99.1)

    return round(num_tests_passed * (100 / num_tests_run), 1)

        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)