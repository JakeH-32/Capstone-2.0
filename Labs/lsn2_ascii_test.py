from cs110 import autograder

def test_passed():
    # Runs the Script
    output, error_message = autograder.run_script("lsn2_ascii.py", [])
    
    lines = output.split('\n')
    
    # Checks for the Cat
    if lines[0].rstrip() == '/\\   /\\':
        #test_feedback.write('1')
        if lines[1].rstrip() == '  o o':
            #test_feedback.write('2')
            if lines[2].rstrip() == ' =   =':
                #test_feedback.write('3')
                if lines[3].rstrip() == '  ---':
                    #test_feedback.write('4')
                    print('Cat Looks Good!\n')
                    return 100
                else:
                    print('Problem in the fourth line of the cat') 
            else:
                print('Problem in the third line of the cat')  
        else:
            print('Problem in the second line of the cat')  
    else:
        print('Problem in the first line of the cat')
    
    return 0

# Testbench (to be run in an IDE)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)