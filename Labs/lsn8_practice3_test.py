from cs110 import autograder
import random, math

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    score = 0
    
    dollar_amount = round(random.uniform(1.00, 1000.00), 2)
    pound_amount = dollar_amount / 1.25
    won_amount = dollar_amount / 0.00083
    peso_amount = won_amount / 53.81
    
    output, error_message = autograder.run_script("lsn8_practice3.py", [dollar_amount])   
    lines = output.split('\n')
    
    if len(lines) > 0 and autograder.equals(lines[0], pound_amount):
        print("Correct Pound Conversion")
        score += 33
    else:
        print("Incorrect Pound Conversion.  Expected", pound_amount)
        
    if len(lines) > 1 and autograder.equals(lines[1], won_amount):
        print("Correct Won Conversion")
        score += 33
    else:
        print("Incorrect Won Conversion.  Expected", won_amount)
        
    if len(lines) > 2 and autograder.equals(lines[2], peso_amount):
        print("Correct Peso Conversion")
        score += 34
    else:
        print("Incorrect Peso Conversion.  Expected", peso_amount)
    
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


# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------