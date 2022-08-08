import math
from FunctionsWithInputs import greet

greet("Paint Area Calculator")


def paint_calc(height, width, coverage):
    area = height * width
    number_of_cans = math.ceil(area / coverage)
    print(f"You'll need {number_of_cans} cans of paint.")


height_of_wall = int(input("Enter height of the wall. "))
width_of_wall = int(input("Enter width of the wall. "))
coverage = 5


paint_calc(height_of_wall, width_of_wall, coverage)
