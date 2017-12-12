# A tuple that holds today's buffet
foods = ('panner', 'idly', 'dosa', 'poori', 'pizza', 'sandwich')

# Showing them for you
for food in foods:
    print(food)

# If you doubt that the tuples are immutable, try uncommenting
# foods[2] = 'chappati'
# print("\n")

# Creating a new tuple again for buffet
foods = ('chappati', 'idly', 'dosa', 'poori', 'upma', 'sandwich')

# Showing them for you
for food in foods:
    print(food)
