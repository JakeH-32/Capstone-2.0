from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    points_earned = 0
            
    # Runs the Script
    print("-------------------------------")
    print("Test 1 - CS110")
    print("-------------------------------")
    output, error_message = autograder.run_script("lsn5_skill2.py", ["CS110"])
    
    if output.strip() == "You get to program!":
        print("CORRECT\n")
        points_earned += 50
    else:
        print("Incorrect.  Expected: You get to program!\n")
        
    # Runs the Script
    print("-------------------------------")
    print("Test 2 - Another Class")
    print("-------------------------------")
    classes = ['Math 151', 'English 111', 'Physics 110']
    random_class = classes[random.randint(0, len(classes)-1)]
    output, error_message = autograder.run_script("lsn5_skill2.py", [random_class])
    
    if output.strip() == "Boo, no programming.":
        print("CORRECT\n")
        points_earned += 50
    else:
        print("Incorrect.  Expected: Boo, no programming.\n")

    return points_earned


# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)