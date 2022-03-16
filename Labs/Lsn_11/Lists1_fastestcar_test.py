from cs110 import autograder
import random, math
import Lists1_fastestcar

def solution(car1, car2):

    if car1[2] > car2[2]:
        return car1[0]
    elif car2[2] > car1[2]:
        return car2[0]
    else:
        return "Same speed"

def test_passed():
    
    # 5 test strategies
    cars_list = []
    cars_list.append(["Honda Civic", 18983.20, 127])
    cars_list.append(["Acura NSX", 157500.39, 191])
    cars_list.append(["VW Golf GTI", 28595.83, 130])
    cars_list.append(["Ford F-150 Raptor", 45290.82, 107])
    cars_list.append(["Subaru BRZ", 28955.38, 140])
    cars_list.append(["Mazda Mazdaspeed3", 17424.30, 130])
    
    test_vals = []
    
    index_permutations = []
    # build all possible permutations except those with the same vehicle
    for i in range(len(cars_list)):
        for j in range(len(cars_list)):
            if i != j:
                index_permutations.append((i,j))
    
    # randomly choose 4 of the permutations
    for i in range(4):
        car_idx_pair = index_permutations[random.randint(0,len(index_permutations)-1)]
        first_car_idx = car_idx_pair[0]
        second_car_idx = car_idx_pair[1]
        
        index_permutations.remove(car_idx_pair)
        
        test_vals.append([cars_list[first_car_idx], cars_list[second_car_idx]])

    # same speed
    test_vals.append((cars_list[2], cars_list[5]))
  
    i = 0
    total_score = 0.0
    
    for val in test_vals:
        print('-'*10 + "Test #" + str(i) + '-'*10)
        
        output = Lists1_fastestcar.fastest_car(val[0], val[1])
        expected_output = solution(val[0], val[1])

        print("Your Program's Output:")
        print(output)

        if output == None:
            print("INCORRECT - Your function did not return anything. Expected:")
            print(str(expected_output))
        elif output.strip() == expected_output.strip():
            print("CORRECT")
            total_score += 100.0 / len(test_vals)
        else:
            print("INCORRECT - Expected:")
            print(str(expected_output))
            
        print()
        i += 1
    
    return total_score

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