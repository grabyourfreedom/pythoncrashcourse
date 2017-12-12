# Famous rivers and their countries
rivers = {'egypt': "The Nile", 'india': 'The Ganges', 'pakistan': "The Indus"}

for country, river in rivers.items():
    print(river.title() + " runs through " + country.title())

print("Countries")
for country in rivers.keys():
    print(country.title())

print("Rivers")
for river in rivers.values():
    print(river.title())
