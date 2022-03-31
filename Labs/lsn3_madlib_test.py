from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    # Generates Random Values
    first_names = ['Adrian', 'Troy', 'Dave', 'Paul', 'Kelly', 'Steve', 'Barry']
    generic_locations = ['Best Buy', 'AAFES', 'Target', 'THE Walmart', 'Home Depot']
    nouns = ['Video Games', 'Board Games', 'Nintendo Switches', 'Sony PS4s', 'Microsoft (Ugh) Xbox Ones']
    
    first_name = first_names[random.randint(0, len(first_names) - 1)]
    generic_location = generic_locations[random.randint(0, len(generic_locations) - 1)]
    whole_number = random.randint(0, 100)
    plural_noun = nouns[random.randint(0, len(nouns) - 1)]

    expected_output = first_name + ' went to ' + generic_location + ' to buy ' + str(whole_number) + ' different types of ' + plural_noun + "\n"

    # Runs the Script
    output, error_message = autograder.run_script("lsn3_madlib.py", [first_name, generic_location, whole_number, plural_noun])
    
    if output == expected_output:
        print("PASSED!")
        return 100
    else:
        print("String doesn't match.\nExpected: " + expected_output)
        return 0
    

# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)