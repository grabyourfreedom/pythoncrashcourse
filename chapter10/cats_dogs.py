try:
    with open("dogs.txt") as dog_file:
        dogs = dog_file.readlines()

    with open("cats.txt") as cat_file:
        cats = cat_file.readlines()
except FileNotFoundError:
    print("File not found")
else:
    print(dogs)
    print()
    print(cats)