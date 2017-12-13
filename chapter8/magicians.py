# Let's us continue to do some magic with functions
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    i = 0
    while i < len(magicians):
        magicians[i] = magicians[i].title() + " the Great"
        i += 1


magicians = ['sarkar', 'lakshmi']
make_great(magicians)
show_magicians(magicians)