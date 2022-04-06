from cs110 import autograder
import csv

# ---------------------------------------------------------------------
# Lab: Unique Crashes
# Course: CS110, Fall 2020
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Problem Statement:  Create a Python function called get_accident_types
# that takes the name of a file as a parameter.  Your function should return a
# **set** containing all of the unique accident types.
# ---------------------------------------------------------------------


def get_accident_types(fileName):
#     fp = open(fileName, 'r')
#     content = fp.read()

    content = set()
    with open(fileName) as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        for row in csvReader:
            content.add(row[4])
    return content


def main():
    get_accident_types("crashdata_subset1.csv")

