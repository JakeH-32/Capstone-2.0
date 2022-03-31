from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
       
    # Generates Random Values
    distance = random.uniform(100, 200)
    speed = random.uniform(20, 50)
    time = distance / speed
    
    # Runs the Script
    output, error_message = autograder.run_script("lsn4_skill2.py", [distance, speed])
    
    if autograder.equals(output, time):
        print("PASSED")
        return 100
    else:
        print("Incorrect Output, Expected", time)
        return 0


# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)