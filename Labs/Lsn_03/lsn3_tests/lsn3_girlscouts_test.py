from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    # Generates Random Values
    dollar_amount = round(random.uniform(10.00, 100.00), 2)
    super_six_amount = (dollar_amount // 5)
    specialty_amount = (dollar_amount // 6)
    score = 0
    
    line_1 = str(int(super_six_amount)) + " boxes of Thin Mints, Samoas, Tagalongs, Do-Si-Dos, Trefoils, or Savannah Smiles"
    line_2 = str(int(specialty_amount)) + " boxes of S'mores and Toffee-tastic"
    
    # Runs the Script
    output, error_message = autograder.run_script("lsn3_girlscouts.py", [dollar_amount])
    output_lines = output.split('\n')
    
    if line_1 == output_lines[0]:
        print("First Line is Correct")
        score += 50
    else:
        print("First Line is Incorrect.  Expected:", line_1)
    
    if line_2 == output_lines[1]:
        print("Second Line is Correct")
        score += 50
    else:
        print("Second Line is Incorrect.  Expected:", line_2)
    
    return score
    

# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)