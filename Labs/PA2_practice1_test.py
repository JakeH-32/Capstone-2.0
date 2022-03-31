from cs110 import autograder
import PA2_practice1

def add_values(x, y, z):
    return x + y + z

def test_passed():
    
    if 'add_values' in dir(PA2_practice1) and add_values(1, 2, 3) == PA2_practice1.add_values(1, 2, 3):
        print("PASSED")
        return 100.0
    elif 'add_values' not in dir(PA2_practice1):
        print("FAILED.  Could not find function 'add_values'")
    elif result != solution:
        print("FAILED.  Function 'add_values' did not return the correct value")
    else:
        print("FAILED.  Something unexpected happened.")
    
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