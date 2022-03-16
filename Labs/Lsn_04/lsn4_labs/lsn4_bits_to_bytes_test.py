from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    # Generates Random Values
    num_bits = random.randint(1, 1000000)
    num_bytes = num_bits / 8

    # Runs the Script
    output, error_message = autograder.run_script("lsn4_bits_to_bytes.py", [num_bits])
      
    if autograder.equals(output, num_bytes):
        print("Num Bytes Looks Good.")
        return 100.0
    else:
        print("Num Bytes is Incorrect.\nExpected: " + str(num_bytes))
        return 0.0
    

# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)