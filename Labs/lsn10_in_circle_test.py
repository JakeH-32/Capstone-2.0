import lsn10_in_circle
from cs110 import autograder
import random, math

NUM_SUBTESTS = 5
   
def soln(x, y, cir_x, cir_y, radius):
    distance = math.sqrt((cir_x - x)**2 + (cir_y - y)**2)
    return distance <= radius

def test_passed():
    
    passed = 0
    for i in range(NUM_SUBTESTS):
        print('Running sub test %d of %d: ' % (i+1 , NUM_SUBTESTS), end='')
        if i == 0:
            x = 6.04
            y = 2.43
            cir_x = 43.4
            cir_y = 52.2
            radius = 74.1
        else:
            x = random.random() * 10.0
            y = random.random() * 10.0
            cir_x = random.random() * 100.0
            cir_y = random.random() * 100.0
            radius = random.random() * 100.0
        #print(in_circle(x, y, cir_x, cir_y, radius), soln(x, y, cir_x, cir_y, radius))
        if lsn10_in_circle.in_circle(x, y, cir_x, cir_y, radius) == soln(x, y, cir_x, cir_y, radius):
            print("CORRECT!")
            passed += 1
        else:
            print('INCORRECT:  in_circle(%f, %f, %f, %f, %f) incorrectly returned %s' % (x, y, cir_x, cir_y, radius, lsn10_in_circle.in_circle(x, y, cir_x, cir_y, radius)))
    
    return (100 / NUM_SUBTESTS) * passed


# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)