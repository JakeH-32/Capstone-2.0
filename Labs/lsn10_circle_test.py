import lsn10_circle
from cs110 import autograder
import random, math

NUM_SUBTESTS = 5

# Helper method to see if a numeric value is within a specified delta
def soln(radius):
    return math.pi * radius * radius

def test_passed():
    
    passed = 0
    
    print("Feedback:")
    
    for i in range(NUM_SUBTESTS):
        print('Running sub test %d of %d: ' % (i+1 , NUM_SUBTESTS), end='')
        radius = random.random() * 100.0
        if autograder.equals(lsn10_circle.area_circle(radius), soln(radius)):
            print("CORRECT!")
            passed += 1
        else:
            print('area_circle(%d) incorrectly returned' % (radius), lsn10_circle.area_circle(radius))
        
    return round(100 / NUM_SUBTESTS, 1) * passed


# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)