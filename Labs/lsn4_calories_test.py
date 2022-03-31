from cs110 import autograder
import random

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    # Generates Random Values
    age_years = random.randint(10, 99)
    weight_pounds = random.randint(80, 400)
    heart_bpm = random.randint(50, 140)
    time_minutes = random.randint(15, 90)
    
    calories_man   = ( (age_years * 0.2017) + (weight_pounds * 0.09036) + (heart_bpm * 0.6309) - 55.0969 )  * time_minutes / 4.184
    calories_woman = ( (age_years * 0.074)  + (weight_pounds * 0.05741) + (heart_bpm * 0.4472) - 20.4022 ) * time_minutes / 4.184
        
    # Runs the Script
    output, error_message = autograder.run_script("lsn4_calories.py", [age_years, weight_pounds, heart_bpm, time_minutes])
      
    lines = output.split('\n')
      
    if autograder.equals(lines[0], calories_man):
        print("Male Calorie Calculations Look Good.")
        if autograder.equals(lines[1], calories_woman):
            print("Female Calorie Calculations Look Good.")
            return 100.0
        else:
            print("Female Calorie Calculation is Incorrect.\nExpected: " + str(calories_woman))
            return 50.0
    else:
        print("Male Calorie Calculation is Incorrect.\nExpected: " + str(calories_man))
        return 0.0
    

# Runs your code in an IDE (for testing purposes)
if __name__ == '__main__':    
    result = test_passed()
    print("Unit Test Returned:", result)