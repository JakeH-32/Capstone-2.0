from cs110 import autograder
import random, math
import DataStructures_crashes

def solution(filename):
    # Opens the file
    file = open(filename, "r")

    # Extracts ALL of the text as one big string
    file_contents = file.read()

    # Splits the big string into individual lines
    lines = file_contents.split('\n')

    # Creates a Set
    collision_types = set()

    # Looks at every row, and adds the collision type to the set
    # The set automagically prevents duplicates from being added!
    for line in lines:
        columns = line.split(',')
        collision_types.add(columns[4])

    # Returns the set
    return collision_types

# Runs the test
def run_test(filename):
    global tests_passed
    
    result = DataStructures_crashes.get_accident_types(filename)
    expected_value = solution(filename)
    
    if result is None:
        print("Failed on file %s.  Your function did not return anything." % (filename))
    elif type(result) is not set:
        print("Failed on file %s.  Your function did not return a set." % (filename))
    elif result == expected_value:
        print("Passed Test on file", filename, "-- set =", result)
        return 100.0
    else:
        print("Passed Test on file", filename, "-- Your function returned ", result, ", but the answer is", expected_value)

    return 0.0


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    return run_test("crashdata_2003.csv") and run_test("crashdata_2011.csv") and run_test("crashdata_2015.csv")
    
        
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