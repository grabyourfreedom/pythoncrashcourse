# Pet database
tommy = {'animal': 'dog', 'owner': 'jack'}

vision = {'animal': 'cat', 'owner': 'chuck'}

hope = {'animal': 'horse', 'owner': 'dave'}

pets = [tommy, vision, hope]

# Let's print some information about the pets
for pet in pets:
    print("The animal is " + pet['animal'] + " & the owner is " + pet['owner'].title())
