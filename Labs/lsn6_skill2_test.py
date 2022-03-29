from cs110 import autograder
import random, math

num_tests_passed = 0
num_tests_run = 0

# The Actual Solution
def solution(gpa, apa, mpa):
    if gpa < 2.0 or apa < 2.0 or mpa < 2.0:
        return "Probation"
    else:
        return "No Probation"


def run_test(gpa, apa, mpa):
    global num_tests_run, num_tests_passed
    
    num_tests_run += 1
    
    print("--------------------------------------------")
    print("Testing GPA =", str(gpa) + ";", "APA =", str(apa) + ";", "MPA =", mpa)
    print("--------------------------------------------")
    output, error_message = autograder.run_script("lsn6_skill2.py", [gpa, apa, mpa])
        
    print(output.strip())
        
    if output.strip() == solution(gpa, apa, mpa):
        print("SUCCESS!\n")
        num_tests_passed += 1
    else:
        print("INCORRECT.  Expected:", solution(gpa, apa, mpa), "\n")


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    #round(random.uniform(0.1, 1.9),1)
    #round(random.uniform(2.1, 4.0),1)
    run_test(round(random.uniform(2.1, 4.0),1), round(random.uniform(2.1, 4.0),1), round(random.uniform(2.1, 4.0),1))
    run_test(round(random.uniform(0.1, 1.9),1), round(random.uniform(2.1, 4.0),1), round(random.uniform(2.1, 4.0),1))
    run_test(round(random.uniform(2.1, 4.0),1), round(random.uniform(0.1, 1.9),1), round(random.uniform(2.1, 4.0),1))
    run_test(round(random.uniform(2.1, 4.0),1), round(random.uniform(2.1, 4.0),1), round(random.uniform(0.1, 1.9),1))

    return round(num_tests_passed * (100 / num_tests_run), 1)

        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)