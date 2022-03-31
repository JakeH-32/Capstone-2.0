from cs110 import autograder
import random, math

num_tests_passed = 0

# The Actual Solution
def solution(temp, wind):
    if temp < 40:
        if wind < 15:
            return "Parkas"
        else:
            return "OCPs"
    elif temp == 40:
        if wind < 15:
            return 'A-Jackets'
        else:
            return 'OCPs'
    elif temp > 40 and temp <= 60:
        if wind < 15:
            return 'A-Jackets'
        else:
            return 'Parkas'
    else:
        if wind <= 15:
            return 'Blues'
        else:
            return 'A-Jackets'


def run_test(temp, wind):
    global num_tests_passed
    
    print("Testing Temp =", temp, 'and Wind =', wind)
    output, error_message = autograder.run_script("lsn6_uod.py", [temp, wind], False)
    
    print("Output:", output.strip())
    
    if output.strip() == solution(temp, wind):
        print("SUCCESS!\n")
        num_tests_passed += 1
    else:
        print("INCORRECT.  Expected:", solution(temp, wind), "\n")


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    run_test(39, 14)
    run_test(39, 15)
    run_test(39, 16)
    run_test(40, 14)
    run_test(40, 15)
    run_test(40, 16)
    run_test(50, 14)
    run_test(50, 15)
    run_test(50, 16)
    run_test(60, 14)
    run_test(60, 15)
    run_test(60, 16)
    run_test(61, 14)
    run_test(61, 15)
    run_test(61, 16)
    
    return round(num_tests_passed * (100 / 15), 1)

        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)