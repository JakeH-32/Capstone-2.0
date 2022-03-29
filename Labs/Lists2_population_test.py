from cs110 import autograder
import random

def solution(population):
    result = ''
    
    cities_table = [
        ['Tokyo', 37435191],
        ['Delhi', 29399141],
        ['Shanghai', 25647805],
        ['Sao Paulo', 21846507],
        ['Mexico City', 21671908],
        ['Cairo', 20484965],
        ['Dhaka', 20283552],
        ['Mumbai', 20185064],
        ['Beijing', 20035455],
        ['Osaka', 19222665]]
    
    for row in cities_table:
        if row[1] >= population:
            result += row[0] + '\n'
    
    return result.strip()


def test_passed():
    
    random_population_size = random.randint(19, 30) * 1000000
    
    output, error = autograder.run_script("Lists2_population.py", [random_population_size])
    answer = solution(random_population_size)
    
    lines = output.strip().split('\n')
    
    num_matches = autograder.compare_strings(lines, answer.strip().split('\n'))
    
    if num_matches == len(lines):
        print("\nCORRECT")
        return 100.0
    else:
        print("\nOne or more outputs were incorrect.")
        return 0.0
    
        
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