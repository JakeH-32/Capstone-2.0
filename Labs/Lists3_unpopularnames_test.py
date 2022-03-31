from cs110 import autograder
import random, math

expected_output_male = ["ALDO", "ALIJAH", "ALLAN", "ANGEL", "ARTURO", "AUGUSTUS", "BENNETT", "BERISH", "CADEN", "CHRIS", "CODY", "COREY", "DERRICK", "DEVON", "DONOVAN", "EASON", "EDWARD", "ELLIS", "GIOVANI", "HASSAN",]
expected_output_female = ["ABBY", "AIZA", "ALISHA", "ANGELICA", "ANGIE", "ARIANNY", "ARIELA", "ATARA", "AUBREY", "AUTUMN", "AYLA", "BIANCA", "BONNIE", "BRIANNY", "CASSANDRA", "CELIA", "CHAVY", "CHEYENNE", "CORA", "CRISTINA"]

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    if (random.random() > 0.5):
        gender = "MALE"
        expected_output = expected_output_male
    else:
        gender = "FEMALE"
        expected_output = expected_output_female
        
    num_to_print = random.randint(5, 20)
    output, error = autograder.run_script("Lists3_unpopularnames.py", [gender, num_to_print])
    lines = output.strip().split('\n')
    num_matches = autograder.compare_strings(lines, expected_output[:num_to_print])
    
    print()
    
    if len(lines) == 0:
        return 0
    elif len(lines) > len(expected_output[:num_to_print]):
        print("Your program printed more lines than we expected")
        return round(100 * num_matches / len(lines), 1)
    else:
        return round(100.0/len(expected_output[:num_to_print]) * num_matches, 1)

        
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