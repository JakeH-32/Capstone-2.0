from cs110 import autograder
import random, math

# The Actual Solution
def solution(speed):
    # Determines what to return based on the table
    if (speed <= 65):
        return "No Ticket"
    elif (speed >65 and speed <= 70):
        return "Warning"
    elif (speed > 70 and speed <= 75):
        return "Speeding"  
    elif (speed >75 and speed <= 80):
        return "Reckless Driving"
    elif (speed > 80):
        return "Reckless Endangerment"

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    num_tests_passed = 0
    
    SPEEDS_TO_TEST = [random.randint(0, 65),
                      65,
                      random.randint(66, 70),
                      70,
                      random.randint(71, 75),
                      75,
                      random.randint(76, 80),
                      80,
                      random.randint(81, 100)]
    
    for i in range(0, len(SPEEDS_TO_TEST)):
        print("-------------------------------")
        print("Test", i+1)
        print("-------------------------------")
        speed = SPEEDS_TO_TEST[i]
        output, error_message = autograder.run_script("lsn6_speeding.py", [speed])
        
        if output.strip() == solution(speed):
            print("SUCCESS!\n")
            num_tests_passed += 1
        else:
            print("INCORRECT.  Expected:", solution(speed), "\n")
    
    return round(num_tests_passed * (100 / len(SPEEDS_TO_TEST)), 1)

        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)