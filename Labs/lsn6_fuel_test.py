from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    points_earned = 0
            
    # Runs the Script
    print("-------------------------------")
    print("Test 1")
    print("-------------------------------")
    output, error_message = autograder.run_script("lsn6_fuel.py", [30,60])
    
    if output.strip() == "Return to base":
        print("CORRECT\n")
        points_earned += 25
    else:
        print("Incorrect.  Expected: Return to base\n")
        
    # Runs the Script
    print("-------------------------------")
    print("Test 2")
    print("-------------------------------")
    output, error_message = autograder.run_script("lsn6_fuel.py", [60,60])
    
    if output.strip() == "Resume flight":
        print("CORRECT\n")
        points_earned += 25
    else:
        print("Incorrect.  Expected: Resume flight\n")
    
    # Runs the Script
    print("-------------------------------")
    print("Test 3")
    print("-------------------------------")
    output, error_message = autograder.run_script("lsn6_fuel.py", [40,80])
    
    if output.strip() == "Resume flight":
        print("CORRECT\n")
        points_earned += 25
    else:
        print("Incorrect.  Expected: Resume flight\n")

    # Runs the Script
    print("-------------------------------")
    print("Test 4")
    print("-------------------------------")
    output, error_message = autograder.run_script("lsn6_fuel.py", [60,80])
    
    if output.strip() == "Resume flight":
        print("CORRECT\n")
        points_earned += 25
    else:
        print("Incorrect.  Expected: Resume flight\n")

    return points_earned


# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)