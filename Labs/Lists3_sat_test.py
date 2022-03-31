from cs110 import autograder
import random, math

def solution():  
    result = ''
    file = open("sat.csv", "r")
    contents = file.read()
    lines = contents.split("\n")

    sat_table = []
    total = 0

    for line in lines:
        line_components = line.split(',')
        
        school = line_components[0]
        sat_score = int(line_components[1]) + int(line_components[2]) + int(line_components[3])
        total += sat_score
        row = [school, sat_score]
        sat_table.append(row)

    average = total / len(sat_table)

    for row in sat_table:
        if row[1] < average:
            result += str(row[0]) + "\n"

    return result


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    expected_output = solution().strip().split('\n')
    output, error = autograder.run_script("Lists3_sat.py", [])
    lines = output.strip().split('\n')
    num_matches = autograder.compare_strings(lines, expected_output)
    
    print()
    
    if len(lines) == 0:
        return 0
    elif len(lines) > len(expected_output):
        print("Your program printed more lines than we expected")
        return round(100 * num_matches / len(lines), 1)
    else:
        return round(100.0/len(expected_output) * num_matches, 1)

        
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