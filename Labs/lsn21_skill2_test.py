from cs110 import autograder
import random, math
import lsn21_skill2

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    a = random.randint(0, 5)
    b = random.randint(6, 10)
    c = random.randint(100, 200)
    d = random.randint(0, 99)
    
    score = 0
    
    print("Test #1.  Calling mini_sort(%d, %d)" % (a, b))
    output = lsn21_skill2.mini_sort(a, b)
    print("  Your Function Returned:", output)
    if output == (a, b):
        print("  CORRECT\n")
        score += 50
    else:
        print("  INCORRECT.  Expected", (a, b), "\n")
        
    print("Test #2.  Calling mini_sort(%d, %d)" % (c, d))
    output = lsn21_skill2.mini_sort(c, d)
    print("  Your Function Returned:", output)
    if output == (d, c):
        print("  CORRECT\n")
        score += 50
    else:
        print("  INCORRECT.  Expected", (d, c), "\n")
    
    return score

# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)