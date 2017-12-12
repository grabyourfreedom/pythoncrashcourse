# while loop with three different ways of exiting the loop

while True:
    topping = input("Enter toppings: ")
    if topping == 'quit':
        break
    print("Added " + topping.title())

break_loop = False
while not break_loop:
    topping = input("Enter toppings: ")
    if topping == 'quit':
        break_loop = True
        continue
    print("Added " + topping.title())

topping = ''
while topping != 'quit':
    topping = input("Enter toppings: ")
    if topping == 'quit':
        continue
    print("Added " + topping.title())