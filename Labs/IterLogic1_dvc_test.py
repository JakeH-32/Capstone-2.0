from IterLogic1_dvc import get_years_until
from cs110 import autograder
import random, math

NUM_SUBTESTS = 5

def soln(target_value):
    maintenance_fee = 623.00
    interest_rate = 0.015
    count = 0

    while maintenance_fee < target_value:
        count += 1
        maintenance_fee = maintenance_fee * (1 + interest_rate)
    
    return count

def test_passed():
    passed = 0
    for i in range(NUM_SUBTESTS):
        print('Running test %d of %d:' % (i+1 , NUM_SUBTESTS), end='')
        target_amount = random.randint(650, 1100)
        if autograder.equals(get_years_until(target_amount), soln(target_amount)):
            print("  It will take " + str(get_years_until(target_amount)) + " years until the maintenance fee exceeds $" + str(target_amount))
            passed += 1
        else:
            print('  get_years_until(%d) incorrectly returned %d instead of %d\n' % (target_amount, get_years_until(target_amount), soln(target_amount)))
    
    return round((100 / NUM_SUBTESTS), 1) * passed


# Testbench (to be run on windows)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)





# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------


# --------------------------------------------------
# Downloaded from https://www.autograder.net
# --------------------------------------------------