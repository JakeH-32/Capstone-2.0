from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    # Generates Random Values
    degrees_farenheit = random.random() * 451.0
    degrees_celsius = (degrees_farenheit - 32.0) * 5/9
    degrees_kelvin = degrees_celsius + 273.15
        
    # Runs the Script
    output, error_message = autograder.run_script("lsn4_temperature.py", [degrees_farenheit])
    
    lines = output.split('\n')
    
    if autograder.equals(lines[0], degrees_kelvin):
        print("Conversion to Kelvin looks good.")
        if autograder.equals(lines[1], degrees_celsius):
            print("Conversion to Celsius looks good.")
            return 100.0
        else:
            print("Conversion to Celsius incorrect.\nYour result: " + str(lines[1]) + "\nExpected: " + str(degrees_celsius))
            return 50.0
    else:
        if autograder.equals(lines[0], degrees_celsius):
            print("Looks like you swapped the order of your output. Look at the Problem Statement and try again.")
        else:
            print("Conversion to Kelvin incorrect.\nYour result: " + str(lines[0]) + "\nExpected: " + str(degrees_kelvin))
        return 0.0
    

# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)