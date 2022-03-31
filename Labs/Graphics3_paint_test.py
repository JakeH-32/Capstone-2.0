from cs110 import autograder
import random, math, py_compile

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    try:       
        py_compile.compile("Graphics3_paint.py", doraise=True)
        print("Thank you for your submission. Your instructor will let you know if there is a problem.")
        return 100.0
    except:
        print("There appears to be a syntax error in your code.")
        return 0.0
    
        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)
















# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------


# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------