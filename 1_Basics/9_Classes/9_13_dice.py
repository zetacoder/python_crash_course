"""
9-13. Dice: 

Make a class Die with one attribute called sides, which has a default value of 6. 

Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 

Make a 6-sided die and roll it 10 times.

Make a 10-sided die and a 20-sided die. Roll each die 10 times.

"""
import random as r

class Die:

    def __init__(self, sides = 6):
        self.sides = sides


    def roll_die(self):

        print(r.randint(1, self.sides))

dice_roll_count = 10

die_types = [6, 10 , 20]



for dice_sides in die_types:

    dice_roll = dice_roll_count

    print(f"Rolling the dice with {dice_sides} sides: ")

    while dice_roll > 0:

        d = Die(dice_sides)

        d.roll_die()

        dice_roll -= 1




