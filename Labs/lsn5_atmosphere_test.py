from cs110 import autograder
import random, math

def solution(altitude):
    if altitude >= 0:
        if altitude <= 10:
            return "Troposphere"
    if altitude >= 11:
        if altitude <= 50:
            return "Stratosphere"
    if altitude >= 51:
        if altitude <= 85:
            return "Mesosphere"
    if altitude >= 86:
        if altitude <= 1000:
            return "Thermosphere"
    if altitude >= 1001:
        if altitude <= 100000:
            return "Exosphere"
        else:
            return "Space"
        
# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    TEST_VALUES = [0, 1, 10, 11, 50, 51, 85, 86, 1000, 1001, 100000, 100001]
    tests_passed = 0
    
    for altitude in TEST_VALUES:
        print("--------------------------")
        print("Testing " + str(altitude) + " km")
        print("--------------------------")
        
        # Runs the Script
        output, error_message = autograder.run_script("lsn5_atmosphere.py", [altitude])
                               
        # Your Test Goes Here (Return True if Pass, False Otherwise)   
        if output.strip() == solution(altitude):
            print("Passed\n")
            tests_passed += 1
        else:
            print("Failed (Expected: " + solution(altitude) + ")\n")
    
    print("Passed", tests_passed, "out of", len(TEST_VALUES), "tests.")
    return round(tests_passed * (100 / len(TEST_VALUES)), 2)

        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)