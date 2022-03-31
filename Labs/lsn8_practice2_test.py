from cs110 import autograder
import random, math

num_tests_passed = 0
num_tests_run = 0

def run_test():
    global num_tests_run, num_tests_passed
    
    x1 = round(random.uniform(-10, 10), 1)
    y1 = round(random.uniform(-10, 10), 1)
    x2 = round(random.uniform(-10, 10), 1)
    y2 = round(random.uniform(-10, 10), 1)
    
    num_tests_run += 1
    solution = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
    
    print("--------------------------------------------")
    print("Calculating distance between (%1.1f, %1.1f) and (%1.1f, %1.1f)" % (x1, y1, x2, y2))
    print("--------------------------------------------")
    output, error_message = autograder.run_script("lsn8_practice2.py", [x1, y1, x2, y2], False)
    print("Your Output:", output.strip())
    
    if autograder.equals(output, solution):
        print("CORRECT!\n")
        num_tests_passed += 1
    else:
        print("INCORRECT")    
        print("Expected:", solution)
        print("\n")

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    run_test()
    run_test()

    return round(num_tests_passed * (100 / num_tests_run), 1)

        
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


# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------


# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------