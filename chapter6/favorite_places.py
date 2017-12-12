favorite_places = {'lakshmi': ['madurai', 'kulu', 'kashmir'],
                   'guru': ['wayanad','bangalore'],
                   'viswa': ['kashmir', 'munnar', 'coorg']}

for key,value in favorite_places.items():
    print(key.title() + "'s favorites places are:")
    for place in value:
        print("\t" + place.title())

