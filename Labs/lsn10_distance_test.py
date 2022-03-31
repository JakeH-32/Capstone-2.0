from lsn10_distance import dist_points
from cs110 import autograder
import random, math

NUM_SUBTESTS = 5

def soln(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_passed():
    
    passed = 0
    
    print("Feedback:")
    
    for i in range(NUM_SUBTESTS):
        print('Running sub test %d of %d: ' % (i+1 , NUM_SUBTESTS), end='')
        x1 = round(random.uniform(-10, 10), 1)
        y1 = round(random.uniform(-10, 10), 1)
        x2 = round(random.uniform(-10, 10), 1)
        y2 = round(random.uniform(-10, 10), 1)
        if autograder.equals(dist_points(x1, y1, x2, y2), soln(x1, y1, x2, y2)):
            print("PASSED!")
            passed += 1
        else:
            print('FAILED: dist_point(%1.1f, %1.1f, %1.1f, %1.1f) incorrectly returned' % (x1, y1, x2, y2), dist_points(x1, y1, x2, y2))
    
    return round(100 / NUM_SUBTESTS, 1) * passed


# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)