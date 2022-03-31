from cs110 import autograder
import random, math

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    NUM_TESTS = 5
    num_correct = 0
    
    for i in range(NUM_TESTS):
        # Generates Random Values
        velocity = random.randint(400, 900)
        theta = random.random() * 90.0
        answer = (velocity**2 * math.sin(2 * theta * math.pi/180.0)) / 9.8
        incorrect_degrees_answer = (velocity**2 * math.sin(2 * theta)) / 9.8
            
        print("----------------------------------------")
        print("TEST CASE", i+1)
        print("----------------------------------------")
        
        # Runs the Script
        output, error_message = autograder.run_script("lsn4_projectile.py", [velocity, theta])

        # Optional:  Displays the Error Message (if one is provided)
        if error_message != '':
            print("Error Occurred: " + error_message)    
        
        lines = output.split('\n')
        
        if autograder.equals(lines[0], answer, 10.0):
            print("CORRECT.\n\n")
            num_correct += 1
        elif autograder.equals(lines[0], incorrect_degrees_answer, 10.0):
            print("INCORRECT BUT CLOSE: Using Degrees Instead of Radians for math.sin()")
        else:
            print("INCORRECT (Expected: " + str(answer) + ")\n\n")
    
    return (100 / NUM_TESTS) * num_correct
    

# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)