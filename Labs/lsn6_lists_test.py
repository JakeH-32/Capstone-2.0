from cs110 import autograder
import random, math

num_tests_passed = 0

# The Actual Solution
def solution(gpa, apa, mpa):
    answer = ""
    
    # Determines what output to present (note how we are using the " character because of the 's)
    if (gpa < 3.0 and apa < 3.0 and mpa < 3.0):
        answer += "No List\n"
    elif (gpa >= 3.0 and apa >= 3.0 and mpa >= 3.0):
        answer += "Superintendent's List\n"
    else:
        # Note that these are 3 separate if statements; we do this because we don't know what list(s) the cadet is on
        if (gpa >= 3.0):
            answer += "Dean's List\n"
        
        if (apa >= 3.0):
            answer += "Athletic Director's List\n"
        
        if (mpa >= 3.0):
            answer += "Commandant's List\n"

    return answer.strip()


def run_test(gpa, apa, mpa):
    global num_tests_passed
    
    print("--------------------------------------------")
    print("Testing GPA =", str(gpa) + ";", "APA =", str(apa) + ";", "MPA =", mpa)
    print("--------------------------------------------")
    output, error_message = autograder.run_script("lsn6_lists.py", [gpa, apa, mpa])
        
    if output.strip() == solution(gpa, apa, mpa):
        print("SUCCESS!\n")
        num_tests_passed += 1
    else:
        print("INCORRECT.  Expected:", solution(gpa, apa, mpa), "\n")


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    run_test(2.8, 2.6, 2.5)
    run_test(3.5, 3.2, 2.8)
    run_test(3.3, 2.8, 3.4)
    run_test(3.6, 3.8, 3.2)
    run_test(2.8, 3.5, 3.8)
    
    return round(num_tests_passed * (100 / 5), 1)

        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)