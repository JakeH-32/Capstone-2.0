from cs110 import autograder
import random


# Runs the Python script and sees if it passes the test(s)
def test_passed():
       
    # Generates Random Values
    age = random.randint(18, 30)
    
    # Runs the Script
    output, error_message = autograder.run_script("lsn3_skill2.py", [age])
    
    if autograder.equals(output, age+4):
        print("PASSED")
        return 100
    elif autograder.equals(output, age):
        print("Close!  You forgot to add 4 to the age before printing it out")
        return 50
    else:
        print("Incorrect Output, Expected", age+4)
        return 0


# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)