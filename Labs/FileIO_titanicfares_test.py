from cs110 import autograder
import random, math, os.path

highest_fare = 0
lowest_fare = 9999999

def solution(filename, passenger_class):
    global highest_fare, lowest_fare

    file = open(filename, 'r')
    file_contents = file.read()
    lines_in_file = file_contents.split('\n')
    result = ''

    for line in lines_in_file:
        line_components = line.split(',')
        
        p_class = int(line_components[1])
        fare = float(line_components[7])
        
        if passenger_class == p_class:
            if fare > highest_fare:
                highest_fare = fare
            if fare < lowest_fare:
                lowest_fare = fare

    file.close()


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    score = 0
    random_passenger_class = random.randint(1, 3)
    
    # Deletes Result.txt if it already exists
    if (os.path.exists("result.txt")):
        os.remove("result.txt")
    
    output, error_message = autograder.run_script("FileIO_titanicfares.py", ["titanic2.csv", random_passenger_class])
    
    # Checks to see if the file was created by the program
    if (not os.path.exists("result.txt")):
        print("result.txt is missing")
    else:
        solution("titanic2.csv", random_passenger_class)
        
        file = open("result.txt", "r")
        file_contents = file.read()
        lines = file_contents.strip().split('\n')
        if len(lines) < 2:
            print("Not enough lines in result.txt")
        
        if autograder.equals(lines[0], highest_fare):
            print("Correct Highest Fare")
            score += 50
        else:
            print("Incorrect Highest Fare.  Expected:", highest_fare)
        
        if autograder.equals(lines[1], lowest_fare):
            print("Correct Lowest Fare")
            score += 50
        else:
            print("Incorrect Lowest Fare.  Expected:", lowest_fare)
    
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