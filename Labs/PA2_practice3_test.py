from cs110 import autograder
import random, math

def solution(weights, heights):
    num_thin = 0
    num_healthy = 0
    num_overweight = 0
    num_obese = 0
    
    for i in range(len(weights)):
        bmi = 703 * (weights[i] / heights[i]**2)

        if bmi <= 18.5:
            num_thin += 1
        elif bmi <= 25:
            num_healthy += 1
        elif bmi <= 30:
            num_overweight += 1
        else:
            num_obese += 1
    
    return (num_thin, num_healthy, num_overweight, num_obese)


def test_passed():

    score = 0

    # Generates the Test Set
    num_students = random.randint(5, 10)
    inputs = [num_students]
    weights = []
    heights = []
    
    for i in range(num_students):
        random_weight = random.randint(120, 200)
        random_height = random.randint(55, 76)
        
        weights.append(random_weight)
        heights.append(random_height)
        
        inputs.append(random_weight)
        inputs.append(random_height)
    
    output, error = autograder.run_script("PA2_practice3.py", inputs)
    expected_output = solution(weights, heights)
    
    lines = output.strip().split('\n')
    
    if len(lines) > 0 and autograder.equals(lines[0], expected_output[0]):
        print("Thin is Correct")
        score += 25
    else:
        print("Thin is Incorrect.  Expected", expected_output[0])

    if len(lines) > 1 and autograder.equals(lines[1], expected_output[1]):
        print("Healthy is Correct")
        score += 25
    else:
        print("Healthy is Incorrect.  Expected", expected_output[1])
    
    if len(lines) > 2 and autograder.equals(lines[2], expected_output[2]):
        print("Overweight is Correct")
        score += 25
    else:
        print("Overweight is Incorrect.  Expected", expected_output[2])
    
    if len(lines) > 3 and autograder.equals(lines[3], expected_output[3]):
        print("Obese is Correct")
        score += 25
    else:
        print("Obese is Incorrect.  Expected", expected_output[0])
        
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