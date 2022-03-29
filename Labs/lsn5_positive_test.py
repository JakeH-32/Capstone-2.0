from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    points_earned = 0
    
    # Generates Random Values
    negative_value = random.randint(-100, -1)
    positive_value = random.randint(1, 100)
        
    # Runs the Script
    print("-------------------------------")
    print("# Test 1 - Positive Number")
    print("-------------------------------")
    output, error_message = autograder.run_script("lsn5_positive.py", [positive_value])
    
    if output.strip() == "POSITIVE":
        print("CORRECT\n")
        points_earned += 33
    else:
        print("Incorrect Output:", output)
        print("Expected POSITIVE\n")
        
    
    # Runs the Script
    print("-------------------------------")
    print("# Test 2 - Negative Number")
    print("-------------------------------")
    output, error_message = autograder.run_script("lsn5_positive.py", [negative_value])
    
    if output.strip() == "NOT POSITIVE":
        print("CORRECT\n")
        points_earned += 33
    else:
        print("Incorrect Output:", output)
        print("Expected NOT POSITIVE\n")
        
    
    # Runs the Script
    print("-------------------------------")
    print("# Test 3 - Zero")
    print("-------------------------------")
    output, error_message = autograder.run_script("lsn5_positive.py", [0])
    
    if output.strip() == "NOT POSITIVE":
        print("CORRECT")
        points_earned += 34
    else:
        print("Incorrect Output:", output)
        print("Expected NOT POSITIVE\n")

    return points_earned

# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)