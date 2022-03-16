from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    # Generates Random Values
    distance = round(random.random() * 1000, 1)
    speed = round(random.random() * 60, 1)
    time = distance / speed
    
    # Runs the Script
    output, error_message = autograder.run_script("lsn3_arrivaltime.py", [distance, speed])
    
    if autograder.equals(output, time):
        print("PASSED!")
        return 100
    else:
        print("Value doesn't match.\nExpected: " + str(time))
        return 0
    

# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)
