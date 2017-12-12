# Guess whether a fruit is your favorite
favorite_fruits = ['apple', 'pears', 'bananas', 'watermelon']

fruit = 'pears'
if fruit in favorite_fruits:
    print("You really like " + fruit.title())
else:
    print("Seems like " + fruit.title() + " is not your favorite")
