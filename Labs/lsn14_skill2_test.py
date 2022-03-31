from cs110 import autograder
import random, math, os

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    score = 0.0
    
    # Deletes Result.txt if it already exists
    if (os.path.exists("output.txt")):
        os.remove("output.txt")
    
    output, error_message = autograder.run_script("lsn14_skill2.py", [])
    
    if (os.path.exists("output.txt")):
        print("File Found!")
        score += 50
        file = open("output.txt", "r")
        file_contents = file.read()
        if (len(file_contents) > 0):
            print("File has Something in it!")
            score += 50
        else:
            print("output.txt appears to be empty.  Did you forget to close the file or write to it?")
    else:
        print("File output.txt does not appear to exist")
    
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