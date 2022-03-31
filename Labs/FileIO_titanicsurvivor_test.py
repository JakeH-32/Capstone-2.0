from cs110 import autograder
import random, math, os.path

lowest_fare = 9999999
lowest_fare_name = ''

def solution(filename):
    global lowest_fare, lowest_fare_name

    file = open(filename, 'r')
    file_contents = file.read()
    lines_in_file = file_contents.split('\n')
    result = ''

    for line in lines_in_file:
        line_components = line.split(',')
        
        survived = line_components[0] == '1'
        name = line_components[2]
        fare = float(line_components[7])
        
        if survived == True:
            if fare < lowest_fare:
                lowest_fare = fare
                lowest_fare_name = name

    file.close()


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    score = 0
   
    
    # Deletes Result.txt if it already exists
    if (os.path.exists("result.txt")):
        os.remove("result.txt")
    
    output, error_message = autograder.run_script("FileIO_titanicsurvivor.py", ["titanic2.csv"])
    
    # Checks to see if the file was created by the program
    if (not os.path.exists("result.txt")):
        print("result.txt is missing")
    else:
        solution("titanic2.csv")
        
        file = open("result.txt", "r")
        file_contents = file.read()
        lines = file_contents.strip().split('\n')
        
        if lines[0] == lowest_fare_name:
            print("Correct Passenger")
            score += 50
        else:
            print("Incorrect Passenger", lowest_fare_name)
        
        if autograder.equals(lines[1], lowest_fare):
            print("Correct Lowest Fare")
            score += 50
        else:
            print("Incorrect Lowest Fare.", lowest_fare)
    
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


# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------