# A smart sandwich shop
sandwich_orders = ['veggie', 'pastrami', 'cheese', 'pastrami', 'tuna', 'pastrami']
finished_sandwich = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == 'pastrami':
        print("We ran out of Pastrami")
        continue
    finished_sandwich.append(sandwich)
    print("I made a " + sandwich.title() + " sandwich")

print(finished_sandwich)