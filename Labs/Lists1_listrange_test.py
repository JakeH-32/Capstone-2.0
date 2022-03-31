from cs110 import autograder
import random, math


def solution(test_start, test_stop):
    result = []
    
    result.append(list(range(test_start, test_stop+1)))
    result.append(len(range(test_start, test_stop+1)))
        
    return result

def test_passed():
    
    # 5 test strategies
    test_vals = []
    
    for j in range(5):
        test_val_start = random.randint(0,2048)
        test_val_stop = test_val_start + random.randint(9,16)
        test_vals.append((test_val_start, test_val_stop))
  
    i = 0
    total_score = 0.0
    
    for val in test_vals:
        print('-'*10 + "Test #" + str(i) + '-'*10)
        
        output, error_message = autograder.run_script("Lists1_listrange.py", [val[0], val[1]])
        expected_output = solution(val[0], val[1])
        
        lines = output.strip().split('\n')
        
        if lines[0].strip() == str(expected_output[0]) and autograder.equals(int(lines[1]), expected_output[1]):
            print("CORRECT")
            total_score += 100.0 / len(test_vals)
        else:
            print("INCORRECT")
            
        print()
        i += 1
    
    return total_score

# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)


# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------