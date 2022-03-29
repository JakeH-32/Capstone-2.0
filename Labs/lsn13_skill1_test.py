from cs110 import autograder
import random, math

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    random_multiple = random.randint(1, 10)

    output, error_message = autograder.run_script("lsn13_skill1.py", [random_multiple])
    
    lines = output.strip().split('\n')

    if len(lines) == random_multiple:
        print("CORRECT")
        return 100
    else:
        print("INCORRECT.  Make sure your loop is repeating num_times_to_loop times")
    
    return 0

        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)
