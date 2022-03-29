from cs110 import autograder
import random, math

# The Actual Solution
def draw_tree(num_times):
    result = ""
    for i in range(num_times):
        result += "  *  \n"
        result += " *** \n"
        result += "*****\n"
        result += "  |  \n"
    return result;


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    num_passed = 0
    num_tests = 3
    
    for i in range(num_tests):
        print("-------------------------------------------")
        print("Test", i+1)
        print("-------------------------------------------")
        num_trees = random.randint(0, 5)
        output, error_message = autograder.run_script("lsn9_skill2.py", [num_trees])
        expected_output = draw_tree(num_trees)
        
        if output == expected_output:
            print("Good Job!\n")
            num_passed += 1
        else:
            print("Incorrect Output. Expected the following:")
            print(expected_output, "\n")
    
    return round((100 / num_tests) * num_passed, 1)

        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)