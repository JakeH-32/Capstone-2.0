from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    # Generates Random Values
    num_bits = random.randint(1, 1000000)
    num_bytes = num_bits / 8
    num_kb = num_bytes / 1024
    num_mb = num_kb / 1024
    num_gb = num_mb / 1024
        
    # Runs the Script
    output, error_message = autograder.run_script("lsn4_bits_to_kmg.py", [num_bits])
      
    lines = output.split('\n')
      
    if autograder.equals(lines[0], num_kb):
        print("Kilobyte Conversion Looks Good.")
        if autograder.equals(lines[1], num_mb):
            print("Megabyte Conversion Looks Good.")
            if autograder.equals(lines[2], num_gb):
                print("Gigabyte Conversion Looks Good.")
                return 100.0
            else:
                print("Num GB is Incorrect.\n  Expected: " + str(num_gb))
                return 67.0
        else:
            print("Num MB is Incorrect.\n  Expected: " + str(num_mb))
            return 33.0
    else:
        print("Num KB is Incorrect.\n  Expected: " + str(num_kb))
        return 0.0
    

# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)