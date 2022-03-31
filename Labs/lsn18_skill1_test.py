from cs110 import autograder
import random, math

starship_table = [['Constitution', 288.6,  127.1,  72.6],
                  ['Galaxy',       642.5,  463.73, 135.26],
                  ['Intrepid',     343.0,  133.0,  66],
                  ['Sovereign',   685.3,  250.6,  88.2]]


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    row_to_print = random.randint(0, len(starship_table) - 1)
    col_to_print = random.randint(0, len(starship_table[0]) - 1)
    value_from_table = str(starship_table[row_to_print][col_to_print])
    value_from_table_flipped = str(starship_table[col_to_print][row_to_print])
    output, error = autograder.run_script("lsn18_skill1.py", [row_to_print, col_to_print])
    
    if output.strip() == value_from_table:
        print("CORRECT")
        return 100.0
    elif output.strip() == value_from_table_flipped:
        print("INCORRECT. Expected", value_from_table)
        print("It looks like you flipped columns and rows.  Remember that the format is list_name[row][col]")
        return 25.0
    else:
        print("INCORRECT. Expected", value_from_table)
        print("Try again.  Remember that the format is list_name[row][col]")
        return 0.0
    
        
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