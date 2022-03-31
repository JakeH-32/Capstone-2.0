from cs110 import autograder
import random, math


def run_test(num1, num2, num3):
    print("-------------------------------")
    print("# Testing: " + str(num1) + " " + str(num2) + " " + str(num3))
    print("-------------------------------")
    
    output, error_message = autograder.run_script("lsn5_largest.py", [num1, num2, num3])
    
    if autograder.equals(output, max(num1, num2, num3)):
        print("CORRECT\n")
        return True
    else:
        print("Incorrect.  Expected", max(num1, num2, num3))
        return False


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    tests_passed = 0
    
    # Generate 3 Random Numbers
    num1 = 0
    num2 = 0
    num3 = 0
    
    # Ensures that the 3 Numbers are Different
    while num1 == num2 or num1 == num3 or num2 == num3:
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        num3 = random.randint(0, 100)
    
    # Sorts the numbers
    # This is needed so that we can test relationships between numbers
    numbers = [num1, num2, num3]
    numbers.sort()
    num1 = numbers[0]
    num2 = numbers[1]
    num3 = numbers[2]
    
    # Test 1:  num1, num2, num3
    if run_test(num1, num2, num3):
        tests_passed += 1

    # Test 2:  num1, num3, num2
    if run_test(num1, num3, num2):
        tests_passed += 1
        
    # Test 3:  num2, num3, num1
    if run_test(num2, num3, num1):
        tests_passed += 1
    
    # Test 4:  num3, num1, num2
    if run_test(num3, num1, num2):
        tests_passed += 1

    # Test 5:  num2, num1, num3
    if run_test(num2, num1, num3):
        tests_passed += 1
    
    # Test 6:  3 Equal Numbers
    if run_test(num1, num1, num1):
        tests_passed += 1
            
    print("Passed " + str(tests_passed) + " out of 6 tests")
    return round(tests_passed * (100 / 6), 1)
    
    
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)