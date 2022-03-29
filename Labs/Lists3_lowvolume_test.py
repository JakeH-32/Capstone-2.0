from cs110 import autograder
import random, math

expected_output = [
"700",
"Harbor Ave",
"Woodlawn Ave",
"Root St",
"Calumet Ave",
"Financial PL",
"16th St",
"Racine Ave",
"60th St",
"Wentworth Ave",
"Parnell Ave",
"Ashland Ave",
"Federal St",
"Hamlin Ave",
"Pitney Ct",
"109th St",
"Loomis St",
"Harrison St",
"24th St",
"La Salle St",
"83rd Pl",
"Homan Ave"]


# Runs the Python script and sees if it passes the test(s)
def test_passed():
    output, error = autograder.run_script("Lists3_lowvolume.py", [])
    lines = set(output.split('\n'))
    matches = (len(lines.intersection(expected_output)))
    return (round((matches/22)*100,1))

        
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