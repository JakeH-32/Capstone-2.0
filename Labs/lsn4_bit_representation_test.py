from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    # Generates Random Values
    num_bits = random.randint(1, 32)
    num_colors = 2 ** num_bits

    # Runs the Script
    output, error_message = autograder.run_script("lsn4_bit_representation.py", [num_bits])
      
    if autograder.equals(output, num_colors):
        print("Num Colors Looks Good.")
        return 100.0
    else:
        print("Num Colors is Incorrect.\nExpected: " + str(num_colors))
        return 0.0
    

# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)