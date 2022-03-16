from cs110 import autograder
import random, math

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    score = 0
    
    num_entries = random.randint(1, 6)
    num_above_5000 = random.randint(0, num_entries)
    list_of_values = [num_entries]
    
    for i in range(num_entries):
        if i < num_above_5000:
            list_of_values.append(random.randint(5001, 8000))
        elif i == num_above_5000:
            list_of_values.append(5000)
        else:
            list_of_values.append(random.randint(1, 5000))
    
    average = sum(list_of_values[1:])/num_entries
    min_value = min(list_of_values[1:])
    
    output, error_message = autograder.run_script("IterLogic2_football.py", list_of_values)
    
    lines = output.strip().split('\n')
    last_line = lines[len(lines)-1]

    if len(lines) >= 1 and autograder.equals(lines[0], num_above_5000):
        print("Number Above 5000 Looks Good")
        score += 33
    else:
        print("Number Above 5000 is Incorrect (or Missing)")
    
    if len(lines) >= 2 and autograder.equals(lines[1], average):
        print("Average Looks Good")
        score += 33
    else:
        print("Average is Incorrect (or Missing)")
    
    if len(lines) >= 3 and autograder.equals(lines[2], min_value):
        print("Min Value Looks Good")
        score += 34
    else:
        print("Min Value is Incorrect (or Missing)")
        
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