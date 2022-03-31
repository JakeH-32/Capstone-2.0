from cs110 import autograder
import random, math

num_tests_passed = 0
num_tests_run = 0

def run_test(class_year):
    global num_tests_run, num_tests_passed
    
    num_tests_run += 1
    solution = "Members of the class of " + str(class_year) + " arrived at USAFA in " + str(class_year - 4)
    
    print("--------------------------------------------")
    print("Testing Class Year =", class_year)
    print("--------------------------------------------")
    output, error_message = autograder.run_script("lsn8_practice1.py", [class_year], False)
        
    if output.strip() == solution:
        print("SUCCESS!\n")
        num_tests_passed += 1
    else:
        print("INCORRECT")
        print("Your Output:", output.strip())
        print("Expected:", solution)
        if ".0" in output.strip():
            print("*** HINT:  Is year a floating point number? ***")
        print("\n")

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    run_test(random.randint(1959, 2024))
    run_test(random.randint(1959, 2024))

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