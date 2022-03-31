from cs110 import autograder
import random, math
import lsn10_asteroids 

def soln(ship_x, ship_y, ship_r, asteroid_x, asteroid_y, asteroid_r):
    distance = math.sqrt((ship_x - asteroid_x)**2 + (ship_y - asteroid_y)**2)
    return distance < asteroid_r + ship_r

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    NUM_TESTS = 4
    num_tests_passed = 0
    
    print("Feedback:")
    score = 0
        
    if "dist_points" in dir(lsn10_asteroids):
        score += 20
        print("dist_points function found")
    else:
        print("dist_points function not being utilized.  Don't reinvent the wheel!")
        #score += 20
        
    for i in range(NUM_TESTS):
        print('Running test %d of %d: ' % (i+1 , NUM_TESTS), end='')
        
        if i == 0:
            ship_x = 2.3
            ship_y = 0.2
            ship_r = 3
            asteroid_x = -4
            asteroid_y = 3.4
            asteroid_r = 6
        else:
            ship_x = round(random.uniform(-50, 50), 1)
            ship_y = round(random.uniform(-50, 50), 1)
            ship_r = 3
            asteroid_x = round(random.uniform(-50, 50), 1)
            asteroid_y = round(random.uniform(-50, 50), 1)
            asteroid_r = 6
        
        #print(in_circle(x, y, cir_x, cir_y, radius), soln(x, y, cir_x, cir_y, radius))
        if lsn10_asteroids.detect_collision(ship_x, ship_y, ship_r, asteroid_x, asteroid_y, asteroid_r) == soln(ship_x, ship_y, ship_r, asteroid_x, asteroid_y, asteroid_r):
            print("CORRECT")
            score += 20
        else:
            print('detect_collision(%f, %f, %f, %f, %f, %f) incorrectly returned %s' % (ship_x, ship_y, ship_r, asteroid_x, asteroid_y, asteroid_r, lsn10_asteroids.detect_collision(ship_x, ship_y, ship_r, asteroid_x, asteroid_y, asteroid_r)))
    
    return score
            
            
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)