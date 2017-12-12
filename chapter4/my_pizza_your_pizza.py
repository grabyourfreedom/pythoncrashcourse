pizzas = ['thin', 'cheese', 'crust']
friends_pizza = pizzas[:]
pizzas.append("my pizza")
friends_pizza.append("friends pizza")

print("My favorite pizzas")
for pizza in pizzas:
    print(pizza.title())

print("My friend's favorite pizzas")
for pizza in friends_pizza:
    print(pizza.title())