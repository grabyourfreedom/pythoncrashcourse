# Let's do some custom sandwich
def make_sandwich(*ingredients):
    print("Make a sandwich with following items:")
    for ingredient in ingredients:
        print("\t" + ingredient.title())
    return


make_sandwich('bread', 'cucumber', 'tomato', 'onion')
make_sandwich('wrap', 'cucumber', 'tomato', 'onion', 'tomato')
make_sandwich('bread', 'cucumber', 'tomato', 'onion', 'mushroom', 'olive')