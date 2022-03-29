from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
       
    points_earned = 0   
    
    output, error = autograder.run_script("lsn4_skill1.py", ['abc', 123, 123.45])
    
    lines = output.split("\n")
    
    if (lines[0] == "<class 'str'>"):
        points_earned += 33
        print("my_string correct!")
    else:
        print("my_string is either not present, or is not the correct data type")
    
    if (lines[1] == "<class 'int'>"):
        points_earned += 33
        print("my_integer correct!")
    else:
        print("my_integer is either not present, or is not the correct data type")
        
    if (lines[2] == "<class 'float'>"):
        points_earned += 34
        print("my_float correct!")
    else:
        print("my_float is either not present, or is not the correct data type")
        
    return points_earned


# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)