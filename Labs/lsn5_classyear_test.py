from cs110 import autograder
import random, math


def solution(class_year):
    if class_year < 2022:
        return "Graduate"
    elif class_year == 2022:
        return "Firstie"
    elif class_year == 2023:
        return "Two Degree"
    elif class_year == 2024:
        return "Three Degree"
    elif class_year == 2025:
        return "Four Degree"
    else:
        return "Not a Cadet"

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    START_YEAR = 2021
    END_YEAR = 2026
    number_correct = 0
    
    for year in range(START_YEAR, END_YEAR + 1):
        print("------------------------------")
        print("Testing: " + str(year))
        print("------------------------------")
        
        # Runs the Script
        output, error_message = autograder.run_script("lsn5_classyear.py", [year])
                
        lines = output.split("\n")
               
        if lines[0] == solution(year):
            print("PASS\n")
            number_correct += 1
        else:
            print("FAIL\n")
    
    print("Passed " + str(number_correct) + " out of " + str(END_YEAR - START_YEAR + 1) + " tests")
    return round(number_correct * (100 / (END_YEAR - START_YEAR + 1)), 1)

        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)