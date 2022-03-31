from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    points_earned = 0
            
    # Runs the Script
    print("-------------------------------")
    print("Test 1")
    print("-------------------------------")
    output, error_message = autograder.run_script("lsn6_roundtrip.py", [100,10,30])
    
    if output.strip() == "No Refueling Needed":
        print("CORRECT\n")
        points_earned += 33
    else:
        print("Incorrect.  Expected: No Refueling Needed\n")
        
    # Runs the Script
    print("-------------------------------")
    print("Test 2")
    print("-------------------------------")
    output, error_message = autograder.run_script("lsn6_roundtrip.py", [100,5,20])
    
    if output.strip() == "Refuel on Way Back":
        print("CORRECT\n")
        points_earned += 33
    else:
        print("Incorrect.  Expected: Refuel on Way Back\n")
    
        # Runs the Script
    print("-------------------------------")
    print("Test 3")
    print("-------------------------------")
    output, error_message = autograder.run_script("lsn6_roundtrip.py", [100,7,10])
    
    if output.strip() == "Refuel En Route":
        print("CORRECT\n")
        points_earned += 34
    else:
        print("Incorrect.  Expected: Refuel En Route\n")

    return points_earned


# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)