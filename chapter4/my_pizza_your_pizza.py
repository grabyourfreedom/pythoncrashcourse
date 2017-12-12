# List of pizzas that i like
pizzas = ['thin', 'cheese', 'crust']

# List of pizzas my friend likes
friends_pizza = pizzas[:]

# Adding one of my favorites to the list
pizzas.append("my pizza")

# Adding one of my friend's favorites to the list
friends_pizza.append("friends pizza")

print("My favorite pizzas")
for pizza in pizzas:
    print("\t" + pizza.title())

print("My friend's favorite pizzas")
for pizza in friends_pizza:
    print("\t" + pizza.title())
