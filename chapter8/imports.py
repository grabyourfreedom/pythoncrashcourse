#import unchanged_magicians

#from unchanged_magicians import make_great
#from unchanged_magicians import show_magicians

#from unchanged_magicians import make_great as great
#from unchanged_magicians import show_magicians as show

# import unchanged_magicians as magic

from unchanged_magicians import *
magicians = ['sarkar', 'lakshmi']
copy = make_great(magicians[:])
show_magicians(magicians)
show_magicians(copy)


