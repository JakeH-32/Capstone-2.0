from cs110 import autograder
import random, math

num_tests_passed = 0
num_tests_run = 0

def solution(area_1, area_2, area_3):
    area_1 = area_1 * 0.0015625
    area_3 = area_3 * 0.386102

    if area_1 > area_2 and area_1 > area_3:
        return "Plot 1 is the biggest"
    elif area_2 > area_1 and area_2 > area_3:
        return "Plot 2 is the biggest"
    elif area_3 > area_1 and area_3 > area_2:
        return "Plot 3 is the biggest"
    
    return "This should never return"

def run_test(area1, area2, area3):
    global num_tests_run, num_tests_passed
    
    num_tests_run += 1
    expected_output = solution(area1, area2, area3)
        
    print("--------------------------------------------")
    print("Comparing %1.1f acres, %1.1f sq miles, and %1.1f sq km" % (area1, area2, area3))
    print("--------------------------------------------")
    output, error_message = autograder.run_script("lsn8_practice4.py", [area1, area2, area3])
    
    if output.strip() == expected_output:
        print("CORRECT!\n")
        num_tests_passed += 1
    else:
        print("INCORRECT. Expected:", expected_output)
        print("\n")

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    run_test(random.uniform(100, 1000), random.uniform(0.1, 2.0), random.uniform(0.1, 5.0))
    run_test(random.uniform(100, 1000), random.uniform(0.1, 2.0), random.uniform(0.1, 5.0))
    run_test(random.uniform(100, 1000), random.uniform(0.1, 2.0), random.uniform(0.1, 5.0))

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