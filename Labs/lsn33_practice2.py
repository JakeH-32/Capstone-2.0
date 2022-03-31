from cs110 import autograder

# ---------------------------------------------------------------------
# Lab: Basic Starship Mechanics
# Course: CS110, Fall 2020
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Problem Statement: See Canvas (no seriously, read it)
# ---------------------------------------------------------------------

# This function calculates the amount of time it takes to travel
# an interstellar distance (in light years) at a given warp factor
def calculate_travel_time(warp_factor, distance_in_ly):
    speed_of_light = 3 * 10**5
    ly_in_km = 9.461 * 10**12
    velocity = speed_of_light * warp_factor ** 3.3333
    distance = ly_in_km * distance_in_ly
    return round((distance / velocity) / (24 * 60 * 60), 1)

# Write Your Solution Here