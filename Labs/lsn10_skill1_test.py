from cs110 import autograder
import random, math
from lsn10_skill1 import *

def get_fuel_consumption(distance_in_kilometers):
    distance_in_miles = distance_in_kilometers * 0.621
    return 5 * distance_in_miles

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    score = 0
    
    file = open("lsn10_skill1.py", "r")
    file_contents = file.read()
    num_calls_function1 = file_contents.count("get_fuel_consumption(1500")
    num_calls_function2 = file_contents.count("get_fuel_consumption( 1500")
    num_calls_function3 = file_contents.count("get_fuel_consumption (1500")
    num_calls_function4 = file_contents.count("get_fuel_consumption ( 1500")
    num_calls = num_calls_function1 + num_calls_function2 + num_calls_function3 + num_calls_function4

    output, error_message = autograder.run_script("lsn10_skill1.py", [])
    
    if num_calls >= 1:
        print("get_fuel_consumption called successfully")
        score += 33
    else:
        print("get_fuel_consumption was not called successfully")
    
    if "fuel_consumed" in globals():
        print("fuel_consumed variable successfully created")
        score += 33
    else:
        print("Did not find a variable called fuel_consumed")
        
    if "fuel_consumed" in globals() and fuel_consumed == get_fuel_consumption(1500):
        print("fuel_consumed contains the correct value")
        score += 34
    elif "fuel_consumed" in globals() and fuel_consumed != get_fuel_consumption(1500):
        print("fuel_consumed contains", fuel_consumed, "instead of", get_fuel_consumption(1500))
    else:
        print("Cannot check the value of fuel_consumed because it does not exist")
        
    return score

        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)