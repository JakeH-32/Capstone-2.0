from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    NUM_TESTS = 5
    num_tests_passed = 0

    for i in range(NUM_TESTS):
        print("Running Test " + str(i) + ":")
        
        num_inputs = random.randint(2, 11)
        inputs = [num_inputs]
        sum = 0
        
        for j in range(num_inputs):
            value = random.randint(70, 130)
            sum += value
            inputs.append(value)
               
        avg = sum / (len(inputs) - 1)   
               
        # Runs the Script
        output, error_message = autograder.run_script("IterLogic1_averagerun.py", inputs)
        
        # Extracts the Output
        lines = output.split("\n")
        
        if (len(lines) > 0):            
            if (autograder.equals(lines[0], avg)):
                print("CORRECT\n")
                num_tests_passed += 1
            else:
                print("INCORRECT.  Expected: " + str(avg) + "\n")

    # Result
    return (100 / NUM_TESTS) * num_tests_passed
            

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