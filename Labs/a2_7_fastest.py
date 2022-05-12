from cs110 import autograder
import csv
# ---------------------------------------------------------------------
# Assessment 2, Problem 6
# Course: CS110, Spring 2021
# ---------------------------------------------------------------------

topspeed = 0
pkmn = ""
pkmntype = input()
with open('pokemon.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        if row[2] == pkmntype :
            if int(row[8]) > topspeed :
                topspeed = int(row[8])
                pkmn = row[1]
        
print(topspeed)
print(pkmn)
