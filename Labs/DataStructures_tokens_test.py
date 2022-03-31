from cs110 import autograder
import random, math

def solution(filename, t):
    # Opens the file
    file = open(filename, "r")

    # Extracts ALL of the text as one big string
    file_contents = file.read()

    # Splits the entire document into tokens
    list_of_tokens = file_contents.split(' ')

    # Creates a Dictionary to Store All Tokens
    token_dictionary = {}

    for token in list_of_tokens:
        if token not in token_dictionary:
            token_dictionary[token] = 1
        else:
            token_dictionary[token] = token_dictionary[token] + 1
    
    if t in token_dictionary:
        return token_dictionary[t]
    else:
        return 0
    

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    num_correct = 0
    
    # Test #1:
    print("------------------------------------------")
    print("Test 1")
    print("------------------------------------------")
    answer, error = autograder.run_script("DataStructures_tokens.py", ["review.txt", "Fit"])
    expected_answer = solution("review.txt", "Fit")
    
    if autograder.equals(answer, expected_answer):
        print("CORRECT\n")
        num_correct += 1
    else:
        print("INCORRECT, Expected:", expected_answer, "\n")
    
    
    # Test #2:
    print("------------------------------------------")
    print("Test 2")
    print("------------------------------------------")
    answer, error = autograder.run_script("DataStructures_tokens.py", ["article.txt", "plastic"])
    expected_answer = solution("article.txt", "plastic")
    
    if autograder.equals(answer, expected_answer):
        print("CORRECT\n")
        num_correct += 1
    else:
        print("INCORRECT, Expected:", expected_answer, "\n")
        
    # Test #3:
    print("------------------------------------------")
    print("Test 3")
    print("------------------------------------------")
    answer, error = autograder.run_script("DataStructures_tokens.py", ["article2.txt", "environment"])
    expected_answer = solution("article2.txt", "environment")
    
    if autograder.equals(answer, expected_answer):
        print("CORRECT")
        num_correct += 1
    else:
        print("INCORRECT, Expected:", expected_answer)
    
    return round(100 / 3 * num_correct, 1)
    
    
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