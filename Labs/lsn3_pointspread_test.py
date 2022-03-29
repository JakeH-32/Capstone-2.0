from cs110 import autograder
import random


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    # Generates Random Values
    score1 = random.randint(0, 50)
    score2 = random.randint(score1, 100)
    spread = abs(score1 - score2)

    points_earned = 0

    # Trial #1:  score 1 > score2
    print("Testing when score 1 is bigger than score 2 . . .")
    output, error_message = autograder.run_script("lsn3_pointspread.py", [score1, score2])
    
    if autograder.equals(output, spread):
        print("PASSED!\n")
        points_earned += 50
    else:
        print("Value doesn't match.\nExpected: " + str(spread)  + "\n")
        
    # Trial #2:  score 2 > score1
    print("Testing when score 2 is bigger than score 1 . . .")
    output, error_message = autograder.run_script("lsn3_pointspread.py", [score2, score1])
    
    if autograder.equals(output, spread):
        print("PASSED!")
        points_earned += 50
    else:
        print("Value doesn't match.\nExpected: " + str(spread))
    
    return points_earned


# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)