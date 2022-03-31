from cs110 import autograder

def test_passed():
    # Runs the Script
    output, error_message = autograder.run_script("lsn2_parking.py", [])
        
    if output.startswith("  NO PARKING\n"):
        if output == "  NO PARKING\n1:00 - 5:00 a.m.\n":
            print("Passed!")
            return 100
        else:
            print("Something is wrong with the second line.")
            return 50
    else:
        print("Something is wrong with the first line.")
        return 0

# Testbench (to be run in an IDE)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)