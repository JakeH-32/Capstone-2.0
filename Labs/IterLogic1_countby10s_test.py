from cs110 import autograder
import random, math

def solution(starting_value, value_to_count_to):
    result = ''
    
    if value_to_count_to < starting_value:
        return "Second integer can't be less than the first."
    else:
        i = starting_value
        
        while i <= value_to_count_to:
            result += str(i) + "\n"
            i += 10
        
        return result

def run_test(random_starting_number, random_ending_number):
    print("#--------------------------------------------")
    print("# Testing", random_starting_number, "to", random_ending_number)
    print("#--------------------------------------------")
    
    output, error_message = autograder.run_script("IterLogic1_countby10s.py", [random_starting_number, random_ending_number])
    expected_output = solution(random_starting_number, random_ending_number)
    
    if output.strip() == expected_output.strip():
        print("CORRECT\n")
        return True
    else:
        print("INCORRECT.  Expected the following:")
        print(expected_output)
        print()
    
    return False

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    score = 0
    
    if run_test(10 * random.randint(1, 5), 60 + 10 * random.randint(1, 20)):
        score += 40
        
    if run_test(random.randint(0, 30), random.randint(31, 200)):
        score += 40
    
    if run_test(random.randint(50, 100), random.randint(0, 10)):
        score += 20
    
    
    return score

        
# Testbench (to be run on windows)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)













# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------


# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------