# A smart sandwich shop
sandwich_orders = ['veggie', 'cheese', 'tune']
finished_sandwich = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwich.append(sandwich)
    print("I made a " + sandwich)

print("\n")
for sandwich in finished_sandwich:
    print(sandwich.title() + " is made")