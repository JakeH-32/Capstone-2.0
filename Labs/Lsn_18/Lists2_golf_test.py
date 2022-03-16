from cs110 import autograder
import random, statistics

random_names = ['Mcllroy', 'Koepka', 'Rahm', 'Woods', 'Thomas', 'Johnson', 'Cantlay', 'Simpson']

def get_random_name():
    global random_names
    name = random_names[random.randint(0, len(random_names)-1)]
    random_names.remove(name)
    return name


def solution(data):
    min_value = 99999
    min_name = ""
    count = 0
    
    for row in data:
        if row[1] < min_value:
            min_value = row[1]
            min_name = row[0]
    
    for row in data:
        if row[1] <= min_value + 5:
            count += 1

    return min_name, (count / len(data) * 100.0)

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    # Generates Random Values
    num_inputs = random.randint(2, 5)
    input_list = []
    data = []
        
    for i in range(num_inputs):
        new_row = [get_random_name(), random.randint(70, 90)]
        input_list.append(new_row[0])
        input_list.append(new_row[1])
        data.append(new_row)
    input_list.append("END")
    
    lowest_name, percent = solution(data)
    
    # Runs the Script
    output, error_message = autograder.run_script("Lists2_golf.py", input_list)
    lines = output.strip().split('\n')

    # Checks Min
    if len(lines) < 2:
        print("Number of output lines does not match")
        return 0
    else:
        if not lowest_name == lines[0]:
            print("Incorrect Name.  Expected " + str(lowest_name))
            return 0
        if not autograder.equals(percent, lines[1]):
            print("Incorrect Percent.  Expected " + str(percent))
            return 50
        
    print("PASSED!")
    return 100
    

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