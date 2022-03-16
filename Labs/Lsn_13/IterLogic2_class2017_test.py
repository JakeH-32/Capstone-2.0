from cs110 import autograder
import random, math

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    score = 0
    
    num_entries = random.randint(1, 6)
    num_in_2017 = random.randint(0, num_entries)
    list_of_values = [num_entries]
    
    for i in range(num_entries):
        if i < num_in_2017:
            list_of_values.append(2017)
        else:
            list_of_values.append(random.randint(2018, 2024))
        
    output, error_message = autograder.run_script("IterLogic2_class2017.py", list_of_values)
    
    lines = output.strip().split('\n')

    if len(lines) >= 1 and autograder.equals(lines[0], num_in_2017):
        print("CORRECT")
        score += 100
    else:
        print("Expected", num_in_2017)
        
    return score
        
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