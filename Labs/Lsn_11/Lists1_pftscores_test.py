from cs110 import autograder
import random, math
#import Lists1_pftscores

pft_scores = [243, 394, 143, 288, 303, 473, 325, 273, 284, 198, 70, 289, 437, 329]


def solution(new_num):
    result = ''
    
    # Append number to num_list ONLY IF IT IS A valid number > 0
    if new_num >= 0 and new_num <= 500:

        temp_scores = pft_scores.copy()
        temp_scores.append(new_num)
        
        average = sum(temp_scores) / len(temp_scores)
        num_range = max(temp_scores) - min(temp_scores)
        
        result += str(average) + '\n'
        result += str(num_range) + '\n'
    else:
        result += "Invalid score provided"
        
    return result

def test_passed():
    
    # 5 test strategies
    # 1) invalid, out of range low
    # 2) invalid, out of range high
    # 3) rand num that doesn't affect range
    # 4) rand num lower than current lowest, but valid
    # 5) rand num higher than current highest, but valid
    
    min_score = min(pft_scores)
    max_score = max(pft_scores)
    
    test_vals = []
    
    # random_low_invalid
    test_vals.append(random.randint(-1010,-1))
    #random_high_invalid
    test_vals.append(random.randint(501,5000))
    #random_mid_num
    test_vals.append(random.randint(min_score, max_score))
    #random_low
    test_vals.append(random.randint(0, min_score-1))
    #random_high
    test_vals.append(random.randint(max_score + 1, 500))
    
    i = 0
    total_score = 0.0
    
    for val in test_vals:
        print('-'*10 + "Test #" + str(i) + '-'*10)
        
        output, error_message = autograder.run_script("Lists1_pftscores.py", [val])
        expected_output = solution(val)
        
        lines = output.strip().split('\n')
        
        if expected_output.strip() == "Invalid score provided":
            if output.strip() == expected_output.strip():
                print("CORRECT")
                total_score += 100 / len(test_vals)
            else:
                print("INCORRECT. Expected the following:")
                print(expected_output)
        else:
            expected_lines = expected_output.strip().split('\n')
            
            if autograder.equals(float(expected_lines[0]), float(lines[0]), 0.99) and autograder.equals(float(expected_lines[1]), float(lines[1]), 0.99):
                print("CORRECT")
                total_score += 100 / len(test_vals)
            else:
                print("INCORRECT. Expected the following:")
                print(expected_output)
            
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