from cs110 import autograder
import random


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    # Generates Random Values
    score1 = random.randint(0, 100)
    score2 = random.randint(0, 100)
    score3 = random.randint(0, 100)
    average = (score1 + score2 + score3) / 3.0
    
    # Runs the Script
    output, error_message = autograder.run_script("lsn3_scoreaverage.py", [score1, score2, score3])
    
    if autograder.equals(output, average):
        print("PASSED!")
        return 100
    else:
        print("Value doesn't match.\nExpected: " + str(average))
        return 0
    

# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)