# A demo to show nested dictionaries - a dictionaries in a dictionary

cities = {'chennai': {'country': 'india', 'population': 7000000,
                      'fact': 'It is in south of India'},
          'boston': {'country': 'united states', 'population': 650000,
                     'fact': 'Boston has european architecture'},
          'karachi': {'country': 'pakistan', 'population': 14000000,
                      'fact': 'It was founded in 1729'},
          }

for city, information in cities.items():
    print(city.title() + "'s details:")
    for key, value in information.items():
        print("\t" + key.title() + ": " + str(value).title())