from cs110 import autograder
import random, math, os.path

num_males = 0
num_females = 0

def solution(filename):
    global num_males, num_females

    input_file = open(filename, "r")
    contents = input_file.read()
    lines = contents.split("\n")

    for line in lines:
        line_components = line.split(',')
        
        if line_components[0] == '1' and line_components[3] == 'male':
            num_males += 1
        if line_components[0] == '1' and line_components[3] == 'female':
            num_females += 1

    input_file.close()


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    score = 0
    
    # Deletes Result.txt if it already exists
    if (os.path.exists("result.txt")):
        os.remove("result.txt")
    
    output, error_message = autograder.run_script("FileIO_survivors_by_gender.py", ["titanic.csv"])
    
    # Checks to see if the file was created by the program
    if (not os.path.exists("result.txt")):
        print("result.txt is missing")
    else:
        solution("titanic.csv")
        
        file = open("result.txt", "r")
        file_contents = file.read()
        lines = file_contents.strip().split('\n')
        if len(lines) < 2:
            print("Not enough lines in result.txt")
        else:    
            if autograder.equals(lines[0], num_males):
                print("Correct Number of Males:")
                score += 50
            else:
                print("Incorrect Number of Males")
            
            if autograder.equals(lines[1], num_females):
                print("Correct Number of Females")
                score += 50
            else:
                print("Incorrect Number of Females")
    
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