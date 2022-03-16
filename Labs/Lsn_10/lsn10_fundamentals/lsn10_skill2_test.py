from cs110 import autograder
import random, math
from lsn10_skill2 import *

def solution(temp_in_f):
    temp_in_k = ((temp_in_f - 32) / 1.8) + 273.15
    return temp_in_k

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    score = 0
    
    print("Feedback:")
    print("Looking for a function called fahrenheit_to_kelvin . . .", end="")
    
    if "fahrenheit_to_kelvin" in globals():
        print("FOUND!")
        score += 50
    else:
        print("NOT FOUND")
    
    random_temp = round(random.uniform(0, 100), 1)
    
    print("Testing function when temperature =", random_temp, "F . . . ", end="")
    if "fahrenheit_to_kelvin" in globals() and fahrenheit_to_kelvin(random_temp) == solution(random_temp):
        print("CORRECT!")
        score += 50
    elif "fahrenheit_to_kelvin" in globals() and fahrenheit_to_kelvin(random_temp) != solution(random_temp):
        print("INCORRECT.  Expected", solution(random_temp), "instead of", fahrenheit_to_kelvin(random_temp))
    else:
        print("Could not evaluate the function's returned value because the function does not exist")
        
    return score

        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)