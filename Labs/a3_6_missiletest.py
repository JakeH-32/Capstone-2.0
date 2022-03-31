from cs110 import autograder

# --------------------------------------------------------------
'''
# Assessment #3, Problem 6

You have been asked to write a program that analyzes number of pushups done by a group of cadets.
Write a program that gets from the user the number of people tested, and gets that many pushup scores
(which you may assume are whole numbers) from the user.  Your program must print out:
The average number of pushups for the group.
The count of cadets that scored higher than the average.
'''
# --------------------------------------------------------------


people = int(input())

scores = []
for i in range(int(people)):
    scores.append(int(input()))
total = 0
for i in range(int(people)):
    total += scores[i]
average = total / people
count = 0
for i in range(int(people)):
    if scores[i] > average:
        count += 1
print(average)
print(count)

