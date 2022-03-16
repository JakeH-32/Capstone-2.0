from cs110 import autograder
import random, math

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    aircraft_dictionary = {"F-16":"Fighting Falcon", "F-22":"Raptor", "B-2":"Spirit", "F-15":"Eagle"}
    
    aircraft = [("C-141", "Starlifter"), ("C-5", "Galaxy"), ("MQ-9", "Reaper")]
    random_aircraft = aircraft[random.randint(0, len(aircraft)-1)]
    aircraft_dictionary[random_aircraft[0]] = random_aircraft[1]
    
    output, error = autograder.run_script("lsn21_skill1.py", random_aircraft)
    
    if output.strip() == str(aircraft_dictionary):
        print("CORRECT")
        return 100.0
    else:
        print("INCORRECT. Expected:")
        print(aircraft_dictionary)
        return 0.0
        
# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)