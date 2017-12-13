from random import randint

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        random_number = randint(1, self.sides)
        print("Number: " + str(random_number))


dice = Dice(20)
i = 1
while i <= 10:
    dice.roll_die()
    i += 1
