from cs110 import autograder
import random, math

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    expected_output = "Lorem ipsum dolor sit amet, qui at luptatum efficiantur, ne autem offendit expetendis mel. Nec augue assentior ea, ne debet virtute mel. Integre vivendo id usu, ne primis repudiandae ullamcorper cum. Harum prompta appellantur vix ut. Ius voluptatibus definitiones te, eius scribentur referrentur mei at. Suas tota velit in usu, ex has complectitur signiferumque, sale lorem dolore ei ius. Perpetua scriptorem mei ex, ex est illum summo consul."
    
    output, error_message = autograder.run_script("lsn14_skill1.py", [])
        
    lines = output.strip().split('\n')
    expected_lines = expected_output.strip().split('\n')
    
    num_matches = autograder.compare_strings(lines, expected_lines)
    
    if num_matches == len(lines):
        print("CORRECT")
        return 100.0
    else:
        print("INCORRECT")
        return 0.0
        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)