from cs110 import autograder
import random
import Lists2_movies

def solution(movies_table, rating, runtime):
    count = 0
    
    for row in movies_table:
        if row[2] == rating and row[3] >= runtime:
            count += 1
    
    return count

# Runs the Python script and sees if it passes the test(s)
def test_passed():
    
    ratings = ['PG', 'PG-13', 'R']
    num_passed = 0
    
    for rating in ratings:
        movies_table = [
            ["Star Wars: A New Hope", 1977, "PG", 121],
            ["Star Trek: The Motion Picture", 1979, "G", 132],
            ["Raiders of the Lost Ark", 1989, "PG", 115],
            ["Indiana Jones and the Temple of Doom", 1984, "PG", 118],
            ["Indiana Jones and the Last Crusade", 1989, "PG-13", 127],
            ["Serenity", 2005, "PG-13", 119],
            ["Joker", 2019, "R", 122],
            ["The Terminator", 1984, "R", 107]
            ]
        test_table = []
        runtime = random.randint(90, 120)
        
        for j in range(random.randint(2, 5)):
            index = random.randint(0, len(movies_table)-1)
            test_table.append(movies_table[index])
            movies_table.remove(movies_table[index])
        
        print("Testing (Rating = " + rating + "):\n" + "  Movie Table: " + str(test_table) + "\n" + "  Runtime: " + str(runtime))
        print("  Expecting: " + str(solution(test_table, rating, runtime)) + "\n  Your Function's Output: " + str(Lists2_movies.get_movies(test_table, rating, runtime)))
        
        if solution(test_table, rating, runtime) == Lists2_movies.get_movies(test_table, rating, runtime):
            print("PASSED!\n")
            num_passed += 1
        else:
            print("INCORRECT\n")
            
    
    return (num_passed / len(ratings)) * 100.0
    

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