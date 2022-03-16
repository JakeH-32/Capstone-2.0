from cs110 import autograder
import lsn9_imagesize, random, math

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    base = random.randint(1024, 1980)
    height = random.randint(1024, 1980)
    bd = 2**random.randint(3, 7)
    output, error_message = autograder.run_script("lsn9_imagesize.py", [base, height, bd])
    
    filesize = (base * height * bd) / 8 / 1024
    score = 0
    
    if "calculate_size_of_image" in dir(lsn9_imagesize):
        print("Function Correctly Defined")
        score += 50
    else:
        print("Function does not exist.  Check to make sure the name matches the prompt")
    
    if autograder.equals(output, filesize):
        print("Function produces correct output")
        score += 50
    else:
        print("Function produces incorrect output. Expected:", filesize)
    
    return score

        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)