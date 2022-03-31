from cs110 import autograder
import random


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    points_earned = 0
    
    # Generates Random Values
    above_freezing = random.uniform(33, 100)
    below_freezing = random.uniform(-100, 31)
    at_freezing    = 32
        
    # Runs the Script
    print("-------------------------------")
    print("Test 1 - Below Freezing")
    print("-------------------------------")
    output, error_message = autograder.run_script("lsn5_skill1.py", [below_freezing])
    
    if output.strip() == "Water Has Frozen":
        print("CORRECT\n")
        points_earned += 33
    else:
        print("Incorrect.  Expected: Water Has Frozen\n")
        
    
    # Runs the Script
    print("-------------------------------")
    print("Test 2 - Above Freezing")
    print("-------------------------------")
    output, error_message = autograder.run_script("lsn5_skill1.py", [above_freezing])
    
    if output.strip() == "Above Water's Freezing Point":
        print("CORRECT\n")
        points_earned += 33
    else:
        print("Incorrect.  Expected: Above Water's Freezing Point\n")
        
    
    # Runs the Script
    print("-------------------------------")
    print("Test 3 - Exactly 32 Degrees")
    print("-------------------------------")
    output, error_message = autograder.run_script("lsn5_skill1.py", [32])
    
    if output.strip() == "Water Has Frozen":
        print("CORRECT")
        points_earned += 34
    else:
        print("Incorrect.  Expected: Water Has Frozen\n")

    return points_earned


# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)