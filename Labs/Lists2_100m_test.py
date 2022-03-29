from cs110 import autograder
import random, statistics

random_names = ['Alice', 'Bob', 'Courtney', 'Devon', 'Frank', 'Genie']

def get_random_name():
    global random_names
    name = random_names[random.randint(0, len(random_names)-1)]
    random_names.remove(name)
    return name

def solution(data):
    fastest_time = 99999
    fastest_squadron = 0
    total = 0
    count = 0
    
    for row in data:
        total += row[2]
        if row[2] <= fastest_time:
            fastest_time = row[2]
            fastest_squadron = row[1]
            
    average = total / len(data)
    
    for row in data:
        if row[2] <= average:
            count += 1
    
    return fastest_squadron, fastest_time, count


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    # Generates Random Values
    num_inputs = random.randint(2, 5)
    input_list = [num_inputs]
    data = []
        
    for i in range(num_inputs):
        new_row = [get_random_name(), random.randint(1, 40), round(random.uniform(12, 18), 1)]
        input_list.append(new_row[0])
        input_list.append(new_row[1])
        input_list.append(new_row[2])
        data.append(new_row)
    
    fastest_squadron, fastest_time, count = solution(data)
    
    # Runs the Script
    output, error_message = autograder.run_script("Lists2_100m.py", input_list)
    lines = output.strip().split('\n')

    # Checks Min
    if len(lines) != 3:
        print("Number of output lines does not match")
        return 0
    else:
        if not autograder.equals(fastest_squadron, lines[0]):
            print("Incorrect Squadron.  Expected " + str(fastest_squadron))
            return 0
        if not autograder.equals(fastest_time, lines[1]):
            print("Incorrect Time.  Expected " + str(fastest_time))
            return 33
        if not autograder.equals(count, lines[2]):
            print("Incorrect Count.  Expected " + str(count))
            return 67
        
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