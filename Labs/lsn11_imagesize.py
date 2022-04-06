from cs110 import autograder

# ---------------------------------------------------------------------
# Lab: Lesson 11 - Image Size
# Course: CS110, Spring 2021
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# PROBLEM STATEMENT:
# Write a function that computes the size of an uncompressed image.
# You will name your function calculate_size_of_image(), and it will have
# three parameters: the width of the image, the height of the image,
# and the bit depth (i.e., # of bits per pixel). The function should print 
# the size of the image, in kilobytes.
# ---------------------------------------------------------------------

# YOUR FUNCTION GOES HERE
   
def calculate_size_of_image(imageW, imageH, imageD):
    kilobytes = (((imageW * imageH * imageD) / 8) / 2**10)
    print(kilobytes)


# Testing Code.  DO NOT TOUCH
if __name__ == "__main__":
    w = int(input())
    h = int(input())
    bd = int(input())
    calculate_size_of_image(w, h, bd)
