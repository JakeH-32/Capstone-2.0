from cs110 import autograder
import random, math

# This function takes a string and prints it backwards
def get_reverse(s):
    result = ''
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    base = round(random.uniform(1.0, 100.0), 1)
    height = round(random.uniform(1.0, 100.0), 1)

    string_list = ['abcde', 'defgh', 'xzy', 'abba']
    test_string = string_list[random.randint(0, len(string_list)-1)]

    file = open("lsn9_callme.py", "r")
    file_contents = file.read()
    num_calls_area_rectangle = file_contents.count("area_rectangle")
    num_calls_print_backwards = file_contents.count("print_backwards")
    num_calls_positive = file_contents.count("positive_or_negative")

    output, error_message = autograder.run_script("lsn9_callme.py", [base, height, test_string])
    
    area = (base * height)
    score = 0
    
    lines = output.split("\n")
    
    if autograder.equals(lines[0], area) and num_calls_area_rectangle > 1:
        print("area_rectangle called successfully")
        score += 33
    else:
        print("area_rectangle was not called successfully")
    
    if len(lines) > 1 and lines[1].strip() == get_reverse(test_string) and num_calls_print_backwards > 1:
        print("print_backwards called successfully")
        score += 33
    else:
        print("print_backwards was not called successfully")
    
    if len(lines) > 2 and lines[2].strip() == "Positive" and num_calls_positive > 1:
        print("positive_or_negative called successfully")
        score += 34
    else:
        print("positive_or_negative was not called successfully")
    
    return score

        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)