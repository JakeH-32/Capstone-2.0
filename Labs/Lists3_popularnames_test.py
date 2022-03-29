from cs110 import autograder
import random, math

expected_output = [
"ISABELLA",
"MIA",
"MOSHE",
"ESTHER",
"SOPHIA",
"EMMA",
"CAMILA",
"CHAYA",
"ETHAN",
"JAYDEN",
"SOFIA",
"AVA",
"JEREMIAH",
"CHAIM",
"JOSE",
"CHANA",
"LUIS",
"ELLA",
"CHARLOTTE",
"HAILEY",
"LEAH",
"MADISON"]


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    num_to_print = random.randint(5, 15)
    output, error = autograder.run_script("Lists3_popularnames.py", [num_to_print])
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