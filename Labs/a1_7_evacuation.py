from cs110 import autograder

# ---------------------------------------------------------------------
# Name: 
# Assessment 1, Problem 5
# Course: CS110, Spring 2021
# ---------------------------------------------------------------------

distance = float(input())

if distance <= 850:
    print("Pipe Bomb")
    print("Suitcase Bomb")
    print("Sedan")
    print("Cargo Van")
    print("Semi-Trailer")
elif distance <= 1850:
    print("Suitcase Bomb")
    print("Sedan")
    print("Cargo Van")
    print("Semi-Trailer")
elif distance <= 2000:
    print("Sedan")
    print("Cargo Van")
    print("Semi-Trailer")
elif distance <= 2750:
    print("Cargo Van")
    print("Semi-Trailer")
elif distance <= 7000:
    print("Semi-Trailer")
else:
    print("Not in range")
