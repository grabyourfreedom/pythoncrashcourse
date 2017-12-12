# Dream Vacation poll, answer this and stand a chance to
# win to your dream location

locations = {}

location = ''
while location != 'quit':
    username = input("Enter your username: ")
    location = input("If you could visit one place in the world, "
                     "where would you go? ")
    if location == 'quit':
        break
    if location not in locations.keys():
        locations[location] = [username]
    else:
        locations[location].append(username)

for name, locations in locations.items():
    print('List of people like ' + name.title())
    for location in locations:
        print("\t" + location)
