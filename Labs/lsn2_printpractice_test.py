from cs110 import autograder

def test_passed():
    # Runs the Script
    output, error_message = autograder.run_script("lsn2_printpractice.py", [])

    student_output = output.strip().split('\n')
    expected_output = ['Welcome to Computer Science 110!', '921600.0', 'Liam is 8 years old', 'F-15  Eagle', 'F-16  Fighting Falcon', 'B-2   Spirit', 'C-141 Starlifter']
    num_matches = autograder.compare_strings(student_output, expected_output)
    
    return round(num_matches * (100 / len(expected_output)), 1)


# Testbench (to be run in an IDE)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)