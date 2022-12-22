import random

feet_in_miles = 5280
meters_in_kilometers = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

# This function simulates rolling dice.

def roll_dice(num):
    return random.randint(1, num)