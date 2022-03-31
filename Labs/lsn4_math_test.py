from cs110 import autograder
import random, math

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    # Generates Random Values
    num1 = random.random() * 100.0
    num2 = random.random() * 100.0
    num3 = random.random() * 10.0
    
    part1 = round(math.sqrt(num1), 2)
    part2 = round(math.fabs(num2 - num3), 2)
    part3 = round(math.factorial(math.ceil(num3)), 2)
    
    # Runs the Script
    output, error_message = autograder.run_script("lsn4_math.py", [num1, num2, num3])
    
    lines = output.split('\n')
    
    correct = [0,0,0]
    
    if autograder.equals(lines[0], part1, 0.001):
        correct[0]=1
        print("Calculation 1 Correct!")
    else:
        print("Calculation 1 Incorrect. Expected: " + str(part1) + "<-- Did you forget to use round()?")
    if autograder.equals(lines[1], part2, 0.001):
        correct[1]=1
        print("Calculation 2 Correct!")
    else:
        print("Calculation 2 Incorrect. Expected: " + str(part2) + "<-- Did you forget to use round()?")
    if autograder.equals(lines[2], part3, 0.001):
        correct[2]=1
        print("Calculation 3 Correct!")
    else:
        print("Calculation 3 Incorrect. Expected: " + str(part3) + "<-- Did you forget to use round()?")
    
    amt_correct = len([elem for elem in correct if elem==1])
    
    return round(amt_correct/3*100,2)
    

# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)